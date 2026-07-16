

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OtherFeesChargesFeeChargeCapItemFeeTypeItem(enum.StrEnum):
    """
    Fee/charge type which is being capped
    """

    SERVICE_C_ACCOUNT_FEE = "ServiceCAccountFee"
    SERVICE_C_ACCOUNT_FEE_MONTHLY = "ServiceCAccountFeeMonthly"
    SERVICE_C_OTHER = "ServiceCOther"
    OTHER = "Other"

    def visit(
        self,
        service_c_account_fee: typing.Callable[[], T_Result],
        service_c_account_fee_monthly: typing.Callable[[], T_Result],
        service_c_other: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObpcaData1OtherFeesChargesFeeChargeCapItemFeeTypeItem.SERVICE_C_ACCOUNT_FEE:
            return service_c_account_fee()
        if self is ObpcaData1OtherFeesChargesFeeChargeCapItemFeeTypeItem.SERVICE_C_ACCOUNT_FEE_MONTHLY:
            return service_c_account_fee_monthly()
        if self is ObpcaData1OtherFeesChargesFeeChargeCapItemFeeTypeItem.SERVICE_C_OTHER:
            return service_c_other()
        if self is ObpcaData1OtherFeesChargesFeeChargeCapItemFeeTypeItem.OTHER:
            return other()
