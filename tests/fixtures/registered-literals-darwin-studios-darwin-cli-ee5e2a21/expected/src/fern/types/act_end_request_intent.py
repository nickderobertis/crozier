

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActEndRequestIntent(enum.StrEnum):
    FINISH = "finish"
    CANCEL = "cancel"

    def visit(self, finish: typing.Callable[[], T_Result], cancel: typing.Callable[[], T_Result]) -> T_Result:
        if self is ActEndRequestIntent.FINISH:
            return finish()
        if self is ActEndRequestIntent.CANCEL:
            return cancel()
