

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateScheduledMessageRequestType(enum.StrEnum):
    """
    The type of scheduled message to be sent. `"direct"` for a direct
    message and `"stream"` or `"channel"` for a channel message.

    Note that, while `"private"` is supported for scheduling direct
    messages, clients are encouraged to use to the modern convention of
    `"direct"` to indicate this message type, because support for
    `"private"` may eventually be removed.

    **Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
    an additional value for this parameter to indicate the type of a channel
    message.
    """

    DIRECT = "direct"
    CHANNEL = "channel"
    STREAM = "stream"
    PRIVATE = "private"

    def visit(
        self,
        direct: typing.Callable[[], T_Result],
        channel: typing.Callable[[], T_Result],
        stream: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateScheduledMessageRequestType.DIRECT:
            return direct()
        if self is CreateScheduledMessageRequestType.CHANNEL:
            return channel()
        if self is CreateScheduledMessageRequestType.STREAM:
            return stream()
        if self is CreateScheduledMessageRequestType.PRIVATE:
            return private()
