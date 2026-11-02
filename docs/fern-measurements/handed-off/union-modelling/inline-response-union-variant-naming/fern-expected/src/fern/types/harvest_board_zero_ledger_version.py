

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HarvestBoardZeroLedgerVersion(enum.StrEnum):
    TWO1 = "2.1"

    def visit(self, two1: typing.Callable[[], T_Result]) -> T_Result:
        if self is HarvestBoardZeroLedgerVersion.TWO1:
            return two1()
