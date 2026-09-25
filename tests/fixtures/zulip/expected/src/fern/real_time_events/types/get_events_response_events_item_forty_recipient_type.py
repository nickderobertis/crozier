

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetEventsResponseEventsItemFortyRecipientType(enum.StrEnum):
    """
    Type of message being composed. Must be `"channel"` or `"direct"`.
    """

    DIRECT = "direct"
    CHANNEL = "channel"

    def visit(self, direct: typing.Callable[[], T_Result], channel: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEventsResponseEventsItemFortyRecipientType.DIRECT:
            return direct()
        if self is GetEventsResponseEventsItemFortyRecipientType.CHANNEL:
            return channel()
