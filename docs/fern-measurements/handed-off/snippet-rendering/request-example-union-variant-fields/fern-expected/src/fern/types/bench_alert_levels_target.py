

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BenchAlertLevelsTarget(enum.StrEnum):
    BENCH = "bench"

    def visit(self, bench: typing.Callable[[], T_Result]) -> T_Result:
        if self is BenchAlertLevelsTarget.BENCH:
            return bench()
