

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarketSelectionStatus(enum.StrEnum):
    CURRENT = "current"
    STALE = "stale"
    MISSING = "missing"
    INVALID = "invalid"

    def visit(
        self,
        current: typing.Callable[[], T_Result],
        stale: typing.Callable[[], T_Result],
        missing: typing.Callable[[], T_Result],
        invalid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarketSelectionStatus.CURRENT:
            return current()
        if self is MarketSelectionStatus.STALE:
            return stale()
        if self is MarketSelectionStatus.MISSING:
            return missing()
        if self is MarketSelectionStatus.INVALID:
            return invalid()
