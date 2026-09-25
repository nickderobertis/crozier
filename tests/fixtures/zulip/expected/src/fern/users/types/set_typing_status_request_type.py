

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SetTypingStatusRequestType(enum.StrEnum):
    """
    Type of the message being composed.

    **Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
    an additional value for this parameter to indicate a channel message is
    being composed.

    In Zulip 8.0 (feature level 215), stopped supporting
    `"private"` as a valid value for this parameter.

    In Zulip 7.0 (feature level 174), `"direct"` was added
    as the preferred way to indicate a direct message is being composed,
    becoming the default value for this parameter and deprecating the
    original `"private"`.

    New in Zulip 4.0 (feature level 58). Previously, typing notifications
    were only for direct messages.
    """

    DIRECT = "direct"
    STREAM = "stream"
    CHANNEL = "channel"

    def visit(
        self,
        direct: typing.Callable[[], T_Result],
        stream: typing.Callable[[], T_Result],
        channel: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SetTypingStatusRequestType.DIRECT:
            return direct()
        if self is SetTypingStatusRequestType.STREAM:
            return stream()
        if self is SetTypingStatusRequestType.CHANNEL:
            return channel()
