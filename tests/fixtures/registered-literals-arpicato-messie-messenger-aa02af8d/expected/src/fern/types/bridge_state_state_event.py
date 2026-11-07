

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BridgeStateStateEvent(enum.StrEnum):
    """
    The current state of this login.
    """

    CONNECTING = "CONNECTING"
    CONNECTED = "CONNECTED"
    TRANSIENT_DISCONNECT = "TRANSIENT_DISCONNECT"
    BAD_CREDENTIALS = "BAD_CREDENTIALS"
    UNKNOWN_ERROR = "UNKNOWN_ERROR"

    def visit(
        self,
        connecting: typing.Callable[[], T_Result],
        connected: typing.Callable[[], T_Result],
        transient_disconnect: typing.Callable[[], T_Result],
        bad_credentials: typing.Callable[[], T_Result],
        unknown_error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BridgeStateStateEvent.CONNECTING:
            return connecting()
        if self is BridgeStateStateEvent.CONNECTED:
            return connected()
        if self is BridgeStateStateEvent.TRANSIENT_DISCONNECT:
            return transient_disconnect()
        if self is BridgeStateStateEvent.BAD_CREDENTIALS:
            return bad_credentials()
        if self is BridgeStateStateEvent.UNKNOWN_ERROR:
            return unknown_error()
