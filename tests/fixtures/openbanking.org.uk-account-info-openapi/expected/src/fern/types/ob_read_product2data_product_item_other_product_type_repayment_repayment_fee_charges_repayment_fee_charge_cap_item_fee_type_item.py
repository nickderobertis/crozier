

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem(
    enum.StrEnum
):
    """
    Fee/charge type which is being capped
    """

    FEPF = "FEPF"
    FTOT = "FTOT"
    FYAF = "FYAF"
    FYAM = "FYAM"
    FYAQ = "FYAQ"
    FYCP = "FYCP"
    FYDB = "FYDB"
    FYMI = "FYMI"
    FYXX = "FYXX"

    def visit(
        self,
        fepf: typing.Callable[[], T_Result],
        ftot: typing.Callable[[], T_Result],
        fyaf: typing.Callable[[], T_Result],
        fyam: typing.Callable[[], T_Result],
        fyaq: typing.Callable[[], T_Result],
        fycp: typing.Callable[[], T_Result],
        fydb: typing.Callable[[], T_Result],
        fymi: typing.Callable[[], T_Result],
        fyxx: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem.FEPF
        ):
            return fepf()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem.FTOT
        ):
            return ftot()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem.FYAF
        ):
            return fyaf()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem.FYAM
        ):
            return fyam()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem.FYAQ
        ):
            return fyaq()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem.FYCP
        ):
            return fycp()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem.FYDB
        ):
            return fydb()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem.FYMI
        ):
            return fymi()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItemFeeTypeItem.FYXX
        ):
            return fyxx()
