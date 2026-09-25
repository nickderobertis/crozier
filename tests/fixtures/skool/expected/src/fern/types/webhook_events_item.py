

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookEventsItem(enum.StrEnum):
    POST = "post"
    COMMENT = "comment"
    CHAT_MESSAGE = "chat_message"
    MEMBER_JOIN = "member_join"
    MEMBER_LEAVE = "member_leave"

    def visit(
        self,
        post: typing.Callable[[], T_Result],
        comment: typing.Callable[[], T_Result],
        chat_message: typing.Callable[[], T_Result],
        member_join: typing.Callable[[], T_Result],
        member_leave: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookEventsItem.POST:
            return post()
        if self is WebhookEventsItem.COMMENT:
            return comment()
        if self is WebhookEventsItem.CHAT_MESSAGE:
            return chat_message()
        if self is WebhookEventsItem.MEMBER_JOIN:
            return member_join()
        if self is WebhookEventsItem.MEMBER_LEAVE:
            return member_leave()
