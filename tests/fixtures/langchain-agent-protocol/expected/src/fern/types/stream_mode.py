

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StreamMode(enum.StrEnum):
    VALUES = "values"
    MESSAGES = "messages"
    UPDATES = "updates"
    CUSTOM = "custom"

    def visit(
        self,
        values: typing.Callable[[], T_Result],
        messages: typing.Callable[[], T_Result],
        updates: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StreamMode.VALUES:
            return values()
        if self is StreamMode.MESSAGES:
            return messages()
        if self is StreamMode.UPDATES:
            return updates()
        if self is StreamMode.CUSTOM:
            return custom()
