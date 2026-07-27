from tools.all_pods import get_all_pods
from tools.all_nodes import get_all_nodes
from tools.all_services import get_all_services
from tools.get_pod_logs import get_pod_logs
from tools.get_unhealthy_pods import get_unhealthy_pods
from tools.describe_pods import describe_pods
from tools.get_cluster_events import get_cluster_events
from tools.get_pod_resource_usage import get_pod_resource_usage


# --------------------------------------------------
# Tool Registry
# --------------------------------------------------

TOOL_REGISTRY = {

    "get_all_pods": get_all_pods,
    "get_all_nodes": get_all_nodes,
    "get_all_services": get_all_services,
    "get_pod_logs": get_pod_logs,
    "get_unhealthy_pods": get_unhealthy_pods,
    "describe_pods": describe_pods,
    "get_cluster_events": get_cluster_events,
    "get_pod_resource_usage": get_pod_resource_usage,

}

# --------------------------------------------------
# Execute Tool
# --------------------------------------------------

def execute_tool(tool_name, **kwargs):
    """
    Executes the selected tool.

    Example:
        execute_tool("get_all_pods")

        execute_tool(
            "get_pod_logs",
            namespace="default",
            pod_name="nginx-7d4f6"
        )

        execute_tool(
            "describe_pods",
            namespace="kube-system",
            pod_name="coredns-xxxx"
        )
    """

    tool = TOOL_REGISTRY.get(tool_name)

    if tool is None:
        return None

    return tool(**kwargs)