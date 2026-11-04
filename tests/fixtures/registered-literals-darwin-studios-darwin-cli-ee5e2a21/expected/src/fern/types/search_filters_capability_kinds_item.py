

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchFiltersCapabilityKindsItem(enum.StrEnum):
    API = "API"
    BROWSER_AUTOMATION = "BROWSER_AUTOMATION"
    MCP = "MCP"
    SOFTWARE_ACTION = "SOFTWARE_ACTION"
    OTHER = "OTHER"

    def visit(
        self,
        api: typing.Callable[[], T_Result],
        browser_automation: typing.Callable[[], T_Result],
        mcp: typing.Callable[[], T_Result],
        software_action: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchFiltersCapabilityKindsItem.API:
            return api()
        if self is SearchFiltersCapabilityKindsItem.BROWSER_AUTOMATION:
            return browser_automation()
        if self is SearchFiltersCapabilityKindsItem.MCP:
            return mcp()
        if self is SearchFiltersCapabilityKindsItem.SOFTWARE_ACTION:
            return software_action()
        if self is SearchFiltersCapabilityKindsItem.OTHER:
            return other()
