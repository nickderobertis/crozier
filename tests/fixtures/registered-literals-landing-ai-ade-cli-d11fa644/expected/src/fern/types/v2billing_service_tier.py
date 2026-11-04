

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2BillingServiceTier(enum.StrEnum):
    STANDARD = "standard"
    PRIORITY = "priority"

    def visit(self, standard: typing.Callable[[], T_Result], priority: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2BillingServiceTier.STANDARD:
            return standard()
        if self is V2BillingServiceTier.PRIORITY:
            return priority()
