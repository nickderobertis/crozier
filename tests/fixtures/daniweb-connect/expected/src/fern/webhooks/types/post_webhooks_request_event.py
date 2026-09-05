

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostWebhooksRequestEvent(enum.StrEnum):
    CONVERSATION_MESSAGE = "conversation_message"
    CONVERSATION_SEEN = "conversation_seen"
    GROUP_UPDATE = "group_update"
    GROUP_MESSAGE = "group_message"
    GROUP_SEEN = "group_seen"
    USER_ONLINE = "user_online"
    USER_UPDATE = "user_update"

    def visit(
        self,
        conversation_message: typing.Callable[[], T_Result],
        conversation_seen: typing.Callable[[], T_Result],
        group_update: typing.Callable[[], T_Result],
        group_message: typing.Callable[[], T_Result],
        group_seen: typing.Callable[[], T_Result],
        user_online: typing.Callable[[], T_Result],
        user_update: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostWebhooksRequestEvent.CONVERSATION_MESSAGE:
            return conversation_message()
        if self is PostWebhooksRequestEvent.CONVERSATION_SEEN:
            return conversation_seen()
        if self is PostWebhooksRequestEvent.GROUP_UPDATE:
            return group_update()
        if self is PostWebhooksRequestEvent.GROUP_MESSAGE:
            return group_message()
        if self is PostWebhooksRequestEvent.GROUP_SEEN:
            return group_seen()
        if self is PostWebhooksRequestEvent.USER_ONLINE:
            return user_online()
        if self is PostWebhooksRequestEvent.USER_UPDATE:
            return user_update()
