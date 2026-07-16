

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod(
    str, enum.Enum
):
    """
    Specifies the period of a fixed length overdraft agreement
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
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.PACT
        ):
            return pact()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.PDAY
        ):
            return pday()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.PHYR
        ):
            return phyr()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.PMTH
        ):
            return pmth()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.PQTR
        ):
            return pqtr()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.PWEK
        ):
            return pwek()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod.PYER
        ):
            return pyer()
