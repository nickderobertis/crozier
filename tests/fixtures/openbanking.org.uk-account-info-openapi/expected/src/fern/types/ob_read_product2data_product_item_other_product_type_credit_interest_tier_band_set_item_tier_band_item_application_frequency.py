

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency(
    enum.StrEnum
):
    """
    How often is interest applied to the Product for this tier/band i.e. how often the financial institution pays accumulated interest to the customer's account.
    """

    FQAT = "FQAT"
    FQDY = "FQDY"
    FQHY = "FQHY"
    FQMY = "FQMY"
    FQOT = "FQOT"
    FQQY = "FQQY"
    FQSD = "FQSD"
    FQWY = "FQWY"
    FQYY = "FQYY"

    def visit(
        self,
        fqat: typing.Callable[[], T_Result],
        fqdy: typing.Callable[[], T_Result],
        fqhy: typing.Callable[[], T_Result],
        fqmy: typing.Callable[[], T_Result],
        fqot: typing.Callable[[], T_Result],
        fqqy: typing.Callable[[], T_Result],
        fqsd: typing.Callable[[], T_Result],
        fqwy: typing.Callable[[], T_Result],
        fqyy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency.FQAT
        ):
            return fqat()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency.FQDY
        ):
            return fqdy()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency.FQHY
        ):
            return fqhy()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency.FQMY
        ):
            return fqmy()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency.FQOT
        ):
            return fqot()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency.FQQY
        ):
            return fqqy()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency.FQSD
        ):
            return fqsd()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency.FQWY
        ):
            return fqwy()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency.FQYY
        ):
            return fqyy()
