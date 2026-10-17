

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CronCreateStreamModeZeroItem(enum.StrEnum):
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
        if self is CronCreateStreamModeZeroItem.VALUES:
            return values()
        if self is CronCreateStreamModeZeroItem.MESSAGES:
            return messages()
        if self is CronCreateStreamModeZeroItem.MESSAGES_TUPLE:
            return messages_tuple()
        if self is CronCreateStreamModeZeroItem.TASKS:
            return tasks()
        if self is CronCreateStreamModeZeroItem.CHECKPOINTS:
            return checkpoints()
        if self is CronCreateStreamModeZeroItem.UPDATES:
            return updates()
        if self is CronCreateStreamModeZeroItem.EVENTS:
            return events()
        if self is CronCreateStreamModeZeroItem.DEBUG:
            return debug()
        if self is CronCreateStreamModeZeroItem.CUSTOM:
            return custom()
