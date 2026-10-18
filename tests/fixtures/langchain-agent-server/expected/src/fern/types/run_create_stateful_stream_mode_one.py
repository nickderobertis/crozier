

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunCreateStatefulStreamModeOne(enum.StrEnum):
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
        if self is RunCreateStatefulStreamModeOne.VALUES:
            return values()
        if self is RunCreateStatefulStreamModeOne.MESSAGES:
            return messages()
        if self is RunCreateStatefulStreamModeOne.MESSAGES_TUPLE:
            return messages_tuple()
        if self is RunCreateStatefulStreamModeOne.TASKS:
            return tasks()
        if self is RunCreateStatefulStreamModeOne.CHECKPOINTS:
            return checkpoints()
        if self is RunCreateStatefulStreamModeOne.UPDATES:
            return updates()
        if self is RunCreateStatefulStreamModeOne.EVENTS:
            return events()
        if self is RunCreateStatefulStreamModeOne.DEBUG:
            return debug()
        if self is RunCreateStatefulStreamModeOne.CUSTOM:
            return custom()
