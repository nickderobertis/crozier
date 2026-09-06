

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class ListActivityLogsResponseItemsItemSource(enum.StrEnum):
    """
    The system that originated the event. `WEBFLOW_AI` for Webflow AI features, `WEBFLOW_MCP` for an external MCP server or Bridge App, `DESIGNER` for human writes from the Designer, and `SYSTEM` for automated Webflow processes such as backups or migrations. `null` for legacy events recorded before attribution was available.
    """

    WEBFLOW_AI = "WEBFLOW_AI"
    WEBFLOW_MCP = "WEBFLOW_MCP"
    DESIGNER = "DESIGNER"
    SYSTEM = "SYSTEM"

    def visit(
        self,
        webflow_ai: typing.Callable[[], T_Result],
        webflow_mcp: typing.Callable[[], T_Result],
        designer: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListActivityLogsResponseItemsItemSource.WEBFLOW_AI:
            return webflow_ai()
        if self is ListActivityLogsResponseItemsItemSource.WEBFLOW_MCP:
            return webflow_mcp()
        if self is ListActivityLogsResponseItemsItemSource.DESIGNER:
            return designer()
        if self is ListActivityLogsResponseItemsItemSource.SYSTEM:
            return system()
