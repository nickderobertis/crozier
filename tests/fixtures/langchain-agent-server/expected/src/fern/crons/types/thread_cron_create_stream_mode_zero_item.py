

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadCronCreateStreamModeZeroItem(enum.StrEnum):
    VALUES = "values"
    MESSAGES = "messages"
    MESSAGES_TUPLE = "messages-tuple"
    TASKS = "tasks"
    CHECKPOINTS = "checkpoints"
    UPDATES = "updates"
    EVENTS = "events"
    DEBUG = "debug"
    CUSTOM = "custom"

    def visit(
        self,
        values: typing.Callable[[], T_Result],
        messages: typing.Callable[[], T_Result],
        messages_tuple: typing.Callable[[], T_Result],
        tasks: typing.Callable[[], T_Result],
        checkpoints: typing.Callable[[], T_Result],
        updates: typing.Callable[[], T_Result],
        events: typing.Callable[[], T_Result],
        debug: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThreadCronCreateStreamModeZeroItem.VALUES:
            return values()
        if self is ThreadCronCreateStreamModeZeroItem.MESSAGES:
            return messages()
        if self is ThreadCronCreateStreamModeZeroItem.MESSAGES_TUPLE:
            return messages_tuple()
        if self is ThreadCronCreateStreamModeZeroItem.TASKS:
            return tasks()
        if self is ThreadCronCreateStreamModeZeroItem.CHECKPOINTS:
            return checkpoints()
        if self is ThreadCronCreateStreamModeZeroItem.UPDATES:
            return updates()
        if self is ThreadCronCreateStreamModeZeroItem.EVENTS:
            return events()
        if self is ThreadCronCreateStreamModeZeroItem.DEBUG:
            return debug()
        if self is ThreadCronCreateStreamModeZeroItem.CUSTOM:
            return custom()
