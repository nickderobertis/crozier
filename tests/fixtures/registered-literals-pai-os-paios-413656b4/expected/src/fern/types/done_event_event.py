

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DoneEventEvent(enum.StrEnum):
    DONE = "done"

    def visit(self, done: typing.Callable[[], T_Result]) -> T_Result:
        if self is DoneEventEvent.DONE:
            return done()
