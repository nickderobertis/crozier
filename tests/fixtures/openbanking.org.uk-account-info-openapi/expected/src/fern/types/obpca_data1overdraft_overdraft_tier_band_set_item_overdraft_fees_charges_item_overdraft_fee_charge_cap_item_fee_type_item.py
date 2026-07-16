

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem(
    str, enum.Enum
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
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.ARRANGED_OVERDRAFT
        ):
            return arranged_overdraft()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.EMERGENCY_BORROWING
        ):
            return emergency_borrowing()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.BORROWING_ITEM
        ):
            return borrowing_item()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.OVERDRAFT_RENEWAL
        ):
            return overdraft_renewal()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.ANNUAL_REVIEW
        ):
            return annual_review()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.OVERDRAFT_SETUP
        ):
            return overdraft_setup()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.SURCHARGE
        ):
            return surcharge()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.TEMP_OVERDRAFT
        ):
            return temp_overdraft()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.UNAUTHORISED_BORROWING
        ):
            return unauthorised_borrowing()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.UNAUTHORISED_PAID_TRANS
        ):
            return unauthorised_paid_trans()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.OTHER
        ):
            return other()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem.UNAUTHORISED_UNPAID_TRANS
        ):
            return unauthorised_unpaid_trans()
