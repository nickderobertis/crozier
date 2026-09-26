

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StreamingChannelZero(enum.StrEnum):
    VALUES = "values"
    UPDATES = "updates"
    MESSAGES = "messages"
    TOOLS = "tools"
    LIFECYCLE = "lifecycle"
    INPUT = "input"
    CHECKPOINTS = "checkpoints"
    TASKS = "tasks"
    CUSTOM = "custom"

    def visit(
        self,
        values: typing.Callable[[], T_Result],
        updates: typing.Callable[[], T_Result],
        messages: typing.Callable[[], T_Result],
        tools: typing.Callable[[], T_Result],
        lifecycle: typing.Callable[[], T_Result],
        input: typing.Callable[[], T_Result],
        checkpoints: typing.Callable[[], T_Result],
        tasks: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StreamingChannelZero.VALUES:
            return values()
        if self is StreamingChannelZero.UPDATES:
            return updates()
        if self is StreamingChannelZero.MESSAGES:
            return messages()
        if self is StreamingChannelZero.TOOLS:
            return tools()
        if self is StreamingChannelZero.LIFECYCLE:
            return lifecycle()
        if self is StreamingChannelZero.INPUT:
            return input()
        if self is StreamingChannelZero.CHECKPOINTS:
            return checkpoints()
        if self is StreamingChannelZero.TASKS:
            return tasks()
        if self is StreamingChannelZero.CUSTOM:
            return custom()
