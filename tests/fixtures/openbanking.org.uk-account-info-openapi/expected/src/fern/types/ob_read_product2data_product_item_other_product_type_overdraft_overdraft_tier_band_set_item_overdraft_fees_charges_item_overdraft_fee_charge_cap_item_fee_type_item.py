

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem(
    str, enum.Enum
):
    """
    Fee/charge type which is being capped
    """

    FBAO = "FBAO"
    FBAR = "FBAR"
    FBEB = "FBEB"
    FBIT = "FBIT"
    FBOR = "FBOR"
    FBOS = "FBOS"
    FBSC = "FBSC"
    FBTO = "FBTO"
    FBUB = "FBUB"
    FBUT = "FBUT"
    FTOT = "FTOT"
    FTUT = "FTUT"

    def visit(
        self,
        fbao: typing.Callable[[], T_Result],
        fbar: typing.Callable[[], T_Result],
        fbeb: typing.Callable[[], T_Result],
        fbit: typing.Callable[[], T_Result],
        fbor: typing.Callable[[], T_Result],
        fbos: typing.Callable[[], T_Result],
        fbsc: typing.Callable[[], T_Result],
        fbto: typing.Callable[[], T_Result],
        fbub: typing.Callable[[], T_Result],
        fbut: typing.Callable[[], T_Result],
        ftot: typing.Callable[[], T_Result],
        ftut: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FBAO
        ):
            return fbao()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FBAR
        ):
            return fbar()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FBEB
        ):
            return fbeb()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FBIT
        ):
            return fbit()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FBOR
        ):
            return fbor()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FBOS
        ):
            return fbos()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FBSC
        ):
            return fbsc()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FBTO
        ):
            return fbto()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FBUB
        ):
            return fbub()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FBUT
        ):
            return fbut()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FTOT
        ):
            return ftot()
        if (
            self
            is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.FTUT
        ):
            return ftut()
