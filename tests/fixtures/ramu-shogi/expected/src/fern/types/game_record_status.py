

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GameRecordStatus(enum.StrEnum):
    FINISHED = "finished"
    ABORTED = "aborted"

    def visit(self, finished: typing.Callable[[], T_Result], aborted: typing.Callable[[], T_Result]) -> T_Result:
        if self is GameRecordStatus.FINISHED:
            return finished()
        if self is GameRecordStatus.ABORTED:
            return aborted()
