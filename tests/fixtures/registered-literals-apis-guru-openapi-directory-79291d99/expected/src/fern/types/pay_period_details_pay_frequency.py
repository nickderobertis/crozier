

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PayPeriodDetailsPayFrequency(enum.StrEnum):
    """
    The frequency at which an individual is paid.
    """

    PAY_FREQUENCY_UNKNOWN = "PAY_FREQUENCY_UNKNOWN"
    PAY_FREQUENCY_WEEKLY = "PAY_FREQUENCY_WEEKLY"
    PAY_FREQUENCY_BIWEEKLY = "PAY_FREQUENCY_BIWEEKLY"
    PAY_FREQUENCY_SEMIMONTHLY = "PAY_FREQUENCY_SEMIMONTHLY"
    PAY_FREQUENCY_MONTHLY = "PAY_FREQUENCY_MONTHLY"

    def visit(
        self,
        pay_frequency_unknown: typing.Callable[[], T_Result],
        pay_frequency_weekly: typing.Callable[[], T_Result],
        pay_frequency_biweekly: typing.Callable[[], T_Result],
        pay_frequency_semimonthly: typing.Callable[[], T_Result],
        pay_frequency_monthly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PayPeriodDetailsPayFrequency.PAY_FREQUENCY_UNKNOWN:
            return pay_frequency_unknown()
        if self is PayPeriodDetailsPayFrequency.PAY_FREQUENCY_WEEKLY:
            return pay_frequency_weekly()
        if self is PayPeriodDetailsPayFrequency.PAY_FREQUENCY_BIWEEKLY:
            return pay_frequency_biweekly()
        if self is PayPeriodDetailsPayFrequency.PAY_FREQUENCY_SEMIMONTHLY:
            return pay_frequency_semimonthly()
        if self is PayPeriodDetailsPayFrequency.PAY_FREQUENCY_MONTHLY:
            return pay_frequency_monthly()
