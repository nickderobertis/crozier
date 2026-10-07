

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ToolDefinitionSource(enum.StrEnum):
    BACKEND = "backend"
    FRONTEND = "frontend"
    MCP = "mcp"

    def visit(
        self,
        backend: typing.Callable[[], T_Result],
        frontend: typing.Callable[[], T_Result],
        mcp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ToolDefinitionSource.BACKEND:
            return backend()
        if self is ToolDefinitionSource.FRONTEND:
            return frontend()
        if self is ToolDefinitionSource.MCP:
            return mcp()
