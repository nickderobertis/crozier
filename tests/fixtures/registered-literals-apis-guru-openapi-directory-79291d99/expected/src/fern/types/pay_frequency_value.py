

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PayFrequencyValue(enum.StrEnum):
    """
    The frequency of the pay period.
    """

    MONTHLY = "monthly"
    SEMIMONTHLY = "semimonthly"
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"
    UNKNOWN = "unknown"

    def visit(
        self,
        monthly: typing.Callable[[], T_Result],
        semimonthly: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        biweekly: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PayFrequencyValue.MONTHLY:
            return monthly()
        if self is PayFrequencyValue.SEMIMONTHLY:
            return semimonthly()
        if self is PayFrequencyValue.WEEKLY:
            return weekly()
        if self is PayFrequencyValue.BIWEEKLY:
            return biweekly()
        if self is PayFrequencyValue.UNKNOWN:
            return unknown()
