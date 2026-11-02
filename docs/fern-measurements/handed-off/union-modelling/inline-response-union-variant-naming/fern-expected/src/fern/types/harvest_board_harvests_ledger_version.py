

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HarvestBoardHarvestsLedgerVersion(enum.StrEnum):
    EMPTY = ""

    def visit(self, empty: typing.Callable[[], T_Result]) -> T_Result:
        if self is HarvestBoardHarvestsLedgerVersion.EMPTY:
            return empty()
