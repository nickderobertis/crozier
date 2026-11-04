

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectorState(enum.StrEnum):
    CREATED = "created"
    AUTH_REQUIRED = "auth_required"
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        auth_required: typing.Callable[[], T_Result],
        connected: typing.Callable[[], T_Result],
        disconnected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectorState.CREATED:
            return created()
        if self is ConnectorState.AUTH_REQUIRED:
            return auth_required()
        if self is ConnectorState.CONNECTED:
            return connected()
        if self is ConnectorState.DISCONNECTED:
            return disconnected()
