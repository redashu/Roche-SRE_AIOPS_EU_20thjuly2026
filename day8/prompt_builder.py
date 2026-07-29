class PromptBuilder:

    def build(
        self,
        user_question,
        retrieved_chunks
    ):

        context = ""

        for index, chunk in enumerate(retrieved_chunks, start=1):

            context += f"""
====================================================
Context {index}

Source: {chunk['filename']}

Content:

{chunk['content']}

"""

        system_prompt = """
You are an experienced Kubernetes Administrator.

You answer ONLY from the provided context.

Rules:

- Use ONLY the retrieved context.
- Never make up information.
- Never use outside knowledge.
- If the answer is unavailable in the context, reply:

"The provided knowledge base does not contain this information."

- Answer professionally.
- Use bullet points whenever appropriate.
"""

        user_prompt = f"""
Retrieved Context

{context}

----------------------------------------------------

User Question

{user_question}
"""

        return {

            "system": [

                {
                    "text": system_prompt
                }

            ],

            "messages": [

                {
                    "role": "user",

                    "content": [

                        {
                            "text": user_prompt
                        }

                    ]
                }

            ]

        }