

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaystubPayFrequency(enum.StrEnum):
    """
    The frequency at which the employee is paid. Possible values: `MONTHLY`, `BI-WEEKLY`, `WEEKLY`, `SEMI-MONTHLY`.
    """

    MONTHLY = "MONTHLY"
    BI_WEEKLY = "BI-WEEKLY"
    WEEKLY = "WEEKLY"
    SEMI_MONTHLY = "SEMI-MONTHLY"

    def visit(
        self,
        monthly: typing.Callable[[], T_Result],
        bi_weekly: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        semi_monthly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaystubPayFrequency.MONTHLY:
            return monthly()
        if self is PaystubPayFrequency.BI_WEEKLY:
            return bi_weekly()
        if self is PaystubPayFrequency.WEEKLY:
            return weekly()
        if self is PaystubPayFrequency.SEMI_MONTHLY:
            return semi_monthly()
