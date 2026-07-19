

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemRole(enum.StrEnum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemRole.USER:
            return user()
        if self is ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemRole.ASSISTANT:
            return assistant()
        if self is ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemRole.SYSTEM:
            return system()
