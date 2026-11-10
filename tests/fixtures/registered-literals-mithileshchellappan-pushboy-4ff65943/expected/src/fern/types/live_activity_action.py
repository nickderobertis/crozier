

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LiveActivityAction(enum.StrEnum):
    START = "start"
    UPDATE = "update"
    END = "end"

    def visit(
        self,
        start: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        end: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LiveActivityAction.START:
            return start()
        if self is LiveActivityAction.UPDATE:
            return update()
        if self is LiveActivityAction.END:
            return end()
