

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class McpAuthStatusStatus(enum.StrEnum):
    """
    Current auth state for this MCP server.
    """

    AUTHENTICATED = "authenticated"
    AUTH_REQUIRED = "auth_required"
    NOT_REQUIRED = "not_required"

    def visit(
        self,
        authenticated: typing.Callable[[], T_Result],
        auth_required: typing.Callable[[], T_Result],
        not_required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is McpAuthStatusStatus.AUTHENTICATED:
            return authenticated()
        if self is McpAuthStatusStatus.AUTH_REQUIRED:
            return auth_required()
        if self is McpAuthStatusStatus.NOT_REQUIRED:
            return not_required()
