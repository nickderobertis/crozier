

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BatchStatus(enum.StrEnum):
    FILLING = "filling"
    CORKED = "corked"

    def visit(self, filling: typing.Callable[[], T_Result], corked: typing.Callable[[], T_Result]) -> T_Result:
        if self is BatchStatus.FILLING:
            return filling()
        if self is BatchStatus.CORKED:
            return corked()
