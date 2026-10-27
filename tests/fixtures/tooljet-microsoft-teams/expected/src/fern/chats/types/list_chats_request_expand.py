

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListChatsRequestExpand(enum.StrEnum):
    MEMBERS = "members"
    LAST_MESSAGE_PREVIEW = "lastMessagePreview"

    def visit(
        self, members: typing.Callable[[], T_Result], last_message_preview: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ListChatsRequestExpand.MEMBERS:
            return members()
        if self is ListChatsRequestExpand.LAST_MESSAGE_PREVIEW:
            return last_message_preview()
