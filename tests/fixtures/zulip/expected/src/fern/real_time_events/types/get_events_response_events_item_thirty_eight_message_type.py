

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemThirtyEightMessageType(enum.StrEnum):
    """
    Type of message being composed. Must be `"stream"` or `"direct"`.

    **Changes**: In Zulip 8.0 (feature level 215), replaced the
    value `"private"` with `"direct"`.

    New in Zulip 4.0 (feature level 58). Previously, all typing
    notifications were implicitly direct messages.
    """

    DIRECT = "direct"
    STREAM = "stream"

    def visit(self, direct: typing.Callable[[], T_Result], stream: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemThirtyEightMessageType.DIRECT:
            return direct()
        if self is GetEventsResponseEventsItemThirtyEightMessageType.STREAM:
            return stream()
