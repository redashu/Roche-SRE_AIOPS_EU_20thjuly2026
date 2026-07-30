import os
import markdown2
from flask import Flask, render_template, request, redirect, url_for, session
from openai import OpenAI
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a strong random secret in production

# ── OpenAI client ──────────────────────────────────────────────
# Set the key in your OS environment before running:
#   Linux/Mac:  export OPENAI_API_KEY="sk-..."
#   Windows:    set OPENAI_API_KEY=sk-...
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env file
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))   

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT", 3306)),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

SYSTEM_PROMPT = (
    "You are a helpful, friendly AI assistant. "
    "Answer the user's questions clearly and concisely."
)

def get_chat_session(user_id):
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT id
        FROM chat_sessions
        WHERE user_id=%s
        ORDER BY id DESC
        LIMIT 1
    """, (user_id,))

    chat = cursor.fetchone()

    if chat:
        chat_session_id = chat["id"]
    else:
        cursor.execute("""
            INSERT INTO chat_sessions(user_id,title)
            VALUES(%s,%s)
        """, (user_id, "Default Chat"))

        db.commit()
        chat_session_id = cursor.lastrowid

    cursor.close()
    return chat_session_id


def load_chat_history(chat_session_id):
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT role, message
        FROM chat_messages
        WHERE session_id=%s
        ORDER BY id
    """, (chat_session_id,))

    history = []

    for row in cursor.fetchall():

        if row["role"] == "assistant":
            history.append({
                "role": "assistant",
                "content": row["message"],
                "html": markdown2.markdown(
                    row["message"],
                    extras=[
                        "fenced-code-blocks",
                        "tables",
                        "strike",
                        "break-on-newline"
                    ]
                )
            })
        else:
            history.append({
                "role": "user",
                "content": row["message"]
            })

    cursor.close()

    return history

def save_message(chat_session_id, role, message):
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO chat_messages(session_id,role,message)
        VALUES(%s,%s,%s)
    """, (chat_session_id, role, message))

    db.commit()
    cursor.close()

def ask_openai(user_message: str, history: list) -> str:
    """
    Send the full conversation history + new user message to OpenAI
    and return the assistant's reply as a string.
    """
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)                          # past turns
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # cheap & fast; swap for "gpt-4o" if you want
        messages=messages,
        max_tokens=1024,
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()


# ── Login ──────────────────────────────────────────────────────
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cursor = db.cursor(dictionary=True)

        query = """
        SELECT *
        FROM users
        WHERE username=%s
        AND password=%s
        """

        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['logged_in'] = True
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['fullname'] = user['fullname']
            session['role'] = user['role']

            chat_session_id = get_chat_session(user['id'])
            session['chat_session_id'] = chat_session_id

            session['history'] = load_chat_history(chat_session_id)

            return redirect(url_for('home'))

        return render_template(
            'index.html',
            error="Invalid username or password"
        )

    return render_template('index.html')
# ── Home / Chat ────────────────────────────────────────────────
@app.route('/home', methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):
        return redirect(url_for('index'))

    user_input = None
    ai_response = None
    error = None

    if request.method == 'POST':
        user_input = request.form.get('user_input', '').strip()

        if user_input:
            history = session.get('history', [])
            chat_session_id = session['chat_session_id']

            try:
                save_message(chat_session_id, "user", user_input)
                ai_response_raw = ask_openai(user_input, history)
                save_message(chat_session_id, "assistant", ai_response_raw)
                

                # Convert Markdown → HTML for clean rendering in the UI
                ai_response = markdown2.markdown(
                    ai_response_raw,
                    extras=["fenced-code-blocks", "tables", "strike", "break-on-newline"]
                )

                # Store raw text for OpenAI context, HTML for display
                history.append({"role": "user",      "content": user_input})
                history.append({"role": "assistant", "content": ai_response_raw, "html": ai_response})

                # Keep last 20 messages (10 turns) to avoid token overflow
                session['history'] = history[-20:]

            except Exception as e:
                error = f"OpenAI error: {str(e)}"

    return render_template(
        'home.html',
        user_input=user_input,
        ai_response=ai_response,
        history=session.get('history', []),
        error=error,
    )


# ── Logout ─────────────────────────────────────────────────────
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5015, host='0.0.0.0')