

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EarningsBreakdownCanonicalDescription(enum.StrEnum):
    """
    Commonly used term to describe the earning line item.
    """

    BONUS = "BONUS"
    COMMISSION = "COMMISSION"
    OVERTIME = "OVERTIME"
    PAID_TIME_OFF = "PAID TIME OFF"
    REGULAR_PAY = "REGULAR PAY"
    VACATION = "VACATION"
    BASIC_ALLOWANCE_HOUSING = "BASIC ALLOWANCE HOUSING"
    BASIC_ALLOWANCE_SUBSISTENCE = "BASIC ALLOWANCE SUBSISTENCE"
    OTHER = "OTHER"

    def visit(
        self,
        bonus: typing.Callable[[], T_Result],
        commission: typing.Callable[[], T_Result],
        overtime: typing.Callable[[], T_Result],
        paid_time_off: typing.Callable[[], T_Result],
        regular_pay: typing.Callable[[], T_Result],
        vacation: typing.Callable[[], T_Result],
        basic_allowance_housing: typing.Callable[[], T_Result],
        basic_allowance_subsistence: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EarningsBreakdownCanonicalDescription.BONUS:
            return bonus()
        if self is EarningsBreakdownCanonicalDescription.COMMISSION:
            return commission()
        if self is EarningsBreakdownCanonicalDescription.OVERTIME:
            return overtime()
        if self is EarningsBreakdownCanonicalDescription.PAID_TIME_OFF:
            return paid_time_off()
        if self is EarningsBreakdownCanonicalDescription.REGULAR_PAY:
            return regular_pay()
        if self is EarningsBreakdownCanonicalDescription.VACATION:
            return vacation()
        if self is EarningsBreakdownCanonicalDescription.BASIC_ALLOWANCE_HOUSING:
            return basic_allowance_housing()
        if self is EarningsBreakdownCanonicalDescription.BASIC_ALLOWANCE_SUBSISTENCE:
            return basic_allowance_subsistence()
        if self is EarningsBreakdownCanonicalDescription.OTHER:
            return other()
