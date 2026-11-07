

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParseBillingServiceTier(enum.StrEnum):
    STANDARD = "standard"
    PRIORITY = "priority"

    def visit(self, standard: typing.Callable[[], T_Result], priority: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParseBillingServiceTier.STANDARD:
            return standard()
        if self is ParseBillingServiceTier.PRIORITY:
            return priority()
