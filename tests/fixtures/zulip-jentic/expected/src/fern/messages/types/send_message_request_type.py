

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SendMessageRequestType(enum.StrEnum):
    """
    The type of message to be sent.

    `"direct"` for a direct message and `"stream"` or `"channel"` for a
    channel message.

    **Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
    an additional value for this parameter to request a channel message.

    In Zulip 7.0 (feature level 174), `"direct"` was added as
    the preferred way to request a direct message, deprecating the original
    `"private"`. While `"private"` is still supported for requesting direct
    messages, clients are encouraged to use to the modern convention with
    servers that support it, because support for `"private"` will eventually
    be removed.
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
        if self is SendMessageRequestType.DIRECT:
            return direct()
        if self is SendMessageRequestType.CHANNEL:
            return channel()
        if self is SendMessageRequestType.STREAM:
            return stream()
        if self is SendMessageRequestType.PRIVATE:
            return private()
