

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod(enum.StrEnum):
    """
    The unit of period (days, weeks, months etc.) of the repayment holiday
    """

    PACT = "PACT"
    PDAY = "PDAY"
    PHYR = "PHYR"
    PMTH = "PMTH"
    PQTR = "PQTR"
    PWEK = "PWEK"
    PYER = "PYER"

    def visit(
        self,
        pact: typing.Callable[[], T_Result],
        pday: typing.Callable[[], T_Result],
        phyr: typing.Callable[[], T_Result],
        pmth: typing.Callable[[], T_Result],
        pqtr: typing.Callable[[], T_Result],
        pwek: typing.Callable[[], T_Result],
        pyer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod.PACT:
            return pact()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod.PDAY:
            return pday()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod.PHYR:
            return phyr()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod.PMTH:
            return pmth()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod.PQTR:
            return pqtr()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod.PWEK:
            return pwek()
        if self is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod.PYER:
            return pyer()
