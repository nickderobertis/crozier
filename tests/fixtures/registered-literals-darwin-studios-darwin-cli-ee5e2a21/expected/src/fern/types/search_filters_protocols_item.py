

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SearchFiltersProtocolsItem(enum.StrEnum):
    DARWIN = "DARWIN"
    UCP = "UCP"
    ACP = "ACP"
    ARD = "ARD"
    A2A = "A2A"
    MCP = "MCP"
    WEBMCP = "WEBMCP"
    OPENAPI = "OPENAPI"
    X402 = "X402"
    MPP = "MPP"
    AP2 = "AP2"

    def visit(
        self,
        darwin: typing.Callable[[], T_Result],
        ucp: typing.Callable[[], T_Result],
        acp: typing.Callable[[], T_Result],
        ard: typing.Callable[[], T_Result],
        a2a: typing.Callable[[], T_Result],
        mcp: typing.Callable[[], T_Result],
        webmcp: typing.Callable[[], T_Result],
        openapi: typing.Callable[[], T_Result],
        x402: typing.Callable[[], T_Result],
        mpp: typing.Callable[[], T_Result],
        ap2: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SearchFiltersProtocolsItem.DARWIN:
            return darwin()
        if self is SearchFiltersProtocolsItem.UCP:
            return ucp()
        if self is SearchFiltersProtocolsItem.ACP:
            return acp()
        if self is SearchFiltersProtocolsItem.ARD:
            return ard()
        if self is SearchFiltersProtocolsItem.A2A:
            return a2a()
        if self is SearchFiltersProtocolsItem.MCP:
            return mcp()
        if self is SearchFiltersProtocolsItem.WEBMCP:
            return webmcp()
        if self is SearchFiltersProtocolsItem.OPENAPI:
            return openapi()
        if self is SearchFiltersProtocolsItem.X402:
            return x402()
        if self is SearchFiltersProtocolsItem.MPP:
            return mpp()
        if self is SearchFiltersProtocolsItem.AP2:
            return ap2()
