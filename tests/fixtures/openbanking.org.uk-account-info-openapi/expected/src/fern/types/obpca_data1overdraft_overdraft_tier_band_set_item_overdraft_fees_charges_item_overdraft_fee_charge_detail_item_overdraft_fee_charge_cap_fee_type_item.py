

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem(
    enum.StrEnum
):
    """
    Overdraft fee type
    """

    ARRANGED_OVERDRAFT = "ArrangedOverdraft"
    EMERGENCY_BORROWING = "EmergencyBorrowing"
    BORROWING_ITEM = "BorrowingItem"
    OVERDRAFT_RENEWAL = "OverdraftRenewal"
    ANNUAL_REVIEW = "AnnualReview"
    OVERDRAFT_SETUP = "OverdraftSetup"
    SURCHARGE = "Surcharge"
    TEMP_OVERDRAFT = "TempOverdraft"
    UNAUTHORISED_BORROWING = "UnauthorisedBorrowing"
    UNAUTHORISED_PAID_TRANS = "UnauthorisedPaidTrans"
    OTHER = "Other"
    UNAUTHORISED_UNPAID_TRANS = "UnauthorisedUnpaidTrans"

    def visit(
        self,
        arranged_overdraft: typing.Callable[[], T_Result],
        emergency_borrowing: typing.Callable[[], T_Result],
        borrowing_item: typing.Callable[[], T_Result],
        overdraft_renewal: typing.Callable[[], T_Result],
        annual_review: typing.Callable[[], T_Result],
        overdraft_setup: typing.Callable[[], T_Result],
        surcharge: typing.Callable[[], T_Result],
        temp_overdraft: typing.Callable[[], T_Result],
        unauthorised_borrowing: typing.Callable[[], T_Result],
        unauthorised_paid_trans: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        unauthorised_unpaid_trans: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.ARRANGED_OVERDRAFT
        ):
            return arranged_overdraft()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.EMERGENCY_BORROWING
        ):
            return emergency_borrowing()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.BORROWING_ITEM
        ):
            return borrowing_item()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.OVERDRAFT_RENEWAL
        ):
            return overdraft_renewal()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.ANNUAL_REVIEW
        ):
            return annual_review()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.OVERDRAFT_SETUP
        ):
            return overdraft_setup()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.SURCHARGE
        ):
            return surcharge()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.TEMP_OVERDRAFT
        ):
            return temp_overdraft()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.UNAUTHORISED_BORROWING
        ):
            return unauthorised_borrowing()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.UNAUTHORISED_PAID_TRANS
        ):
            return unauthorised_paid_trans()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.OTHER
        ):
            return other()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem.UNAUTHORISED_UNPAID_TRANS
        ):
            return unauthorised_unpaid_trans()
