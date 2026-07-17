

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RegionConcurrencyType(enum.StrEnum):
    SEQUENTIAL = "SEQUENTIAL"
    PARALLEL = "PARALLEL"

    def visit(self, sequential: typing.Callable[[], T_Result], parallel: typing.Callable[[], T_Result]) -> T_Result:
        if self is RegionConcurrencyType.SEQUENTIAL:
            return sequential()
        if self is RegionConcurrencyType.PARALLEL:
            return parallel()
