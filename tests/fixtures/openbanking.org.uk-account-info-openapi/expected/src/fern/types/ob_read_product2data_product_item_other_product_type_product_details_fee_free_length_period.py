

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod(enum.StrEnum):
    """
    The unit of period (days, weeks, months etc.) of the promotional length
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
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod.PACT:
            return pact()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod.PDAY:
            return pday()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod.PHYR:
            return phyr()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod.PMTH:
            return pmth()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod.PQTR:
            return pqtr()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod.PWEK:
            return pwek()
        if self is ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod.PYER:
            return pyer()
