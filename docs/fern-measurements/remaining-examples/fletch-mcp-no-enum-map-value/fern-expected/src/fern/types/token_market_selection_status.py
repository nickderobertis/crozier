

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenMarketSelectionStatus(enum.StrEnum):
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
        if self is TokenMarketSelectionStatus.CURRENT:
            return current()
        if self is TokenMarketSelectionStatus.STALE:
            return stale()
        if self is TokenMarketSelectionStatus.MISSING:
            return missing()
        if self is TokenMarketSelectionStatus.INVALID:
            return invalid()
