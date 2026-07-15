

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MessageDirection(str, enum.Enum):
    """
    The direction of the message.
    """

    INBOUND = "inbound"
    OUTBOUND_API = "outbound-api"
    OUTBOUND_CALL = "outbound-call"
    OUTBOUND_REPLY = "outbound-reply"
    UNKNOWN = "unknown"

    def visit(
        self,
        inbound: typing.Callable[[], T_Result],
        outbound_api: typing.Callable[[], T_Result],
        outbound_call: typing.Callable[[], T_Result],
        outbound_reply: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageDirection.INBOUND:
            return inbound()
        if self is MessageDirection.OUTBOUND_API:
            return outbound_api()
        if self is MessageDirection.OUTBOUND_CALL:
            return outbound_call()
        if self is MessageDirection.OUTBOUND_REPLY:
            return outbound_reply()
        if self is MessageDirection.UNKNOWN:
            return unknown()
