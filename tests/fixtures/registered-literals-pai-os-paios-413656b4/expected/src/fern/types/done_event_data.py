

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DoneEventData(enum.StrEnum):
    DONE = "[DONE]"

    def visit(self, done: typing.Callable[[], T_Result]) -> T_Result:
        if self is DoneEventData.DONE:
            return done()
