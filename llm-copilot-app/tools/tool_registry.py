from tools.all_pods import get_all_pods
from tools.all_nodes import get_all_nodes
from tools.all_services import get_all_services
from tools.all_deployments import get_all_deployments
from tools.get_unhealthy_pods import get_unhealthy_pods
from tools.get_cluster_events import get_cluster_events


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "get_all_pods": get_all_pods,
            "get_all_nodes": get_all_nodes,
            "get_all_services": get_all_services,
            "get_all_deployments": get_all_deployments,
            "get_unhealthy_pods": get_unhealthy_pods,
            "get_cluster_events": get_cluster_events
        }

    def execute(self, tool_name):

        tool = self.tools.get(tool_name)

        if tool is None:
            raise Exception(f"Unknown Tool : {tool_name}")

        return tool()

    def list_tools(self):

        return list(self.tools.keys())