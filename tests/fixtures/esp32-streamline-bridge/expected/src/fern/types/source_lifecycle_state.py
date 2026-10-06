

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SourceLifecycleState(enum.StrEnum):
    PENDING = "pending"
    CONNECTED = "connected"
    HTTP_SELECTED = "http-selected"
    ALLOWLISTED = "allowlisted"
    DISCONNECTED = "disconnected"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        connected: typing.Callable[[], T_Result],
        http_selected: typing.Callable[[], T_Result],
        allowlisted: typing.Callable[[], T_Result],
        disconnected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SourceLifecycleState.PENDING:
            return pending()
        if self is SourceLifecycleState.CONNECTED:
            return connected()
        if self is SourceLifecycleState.HTTP_SELECTED:
            return http_selected()
        if self is SourceLifecycleState.ALLOWLISTED:
            return allowlisted()
        if self is SourceLifecycleState.DISCONNECTED:
            return disconnected()
