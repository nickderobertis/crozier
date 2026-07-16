

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem(str, enum.Enum):
    """
    Fee/charge type which is being capped
    """

    OTHER = "Other"
    SERVICE_C_ACCOUNT_FEE = "ServiceCAccountFee"
    SERVICE_C_ACCOUNT_FEE_MONTHLY = "ServiceCAccountFeeMonthly"
    SERVICE_C_ACCOUNT_FEE_QUARTERLY = "ServiceCAccountFeeQuarterly"
    SERVICE_C_FIXED_TARIFF = "ServiceCFixedTariff"
    SERVICE_C_BUSI_DEP_ACC_BREAKAGE = "ServiceCBusiDepAccBreakage"
    SERVICE_C_MINIMUM_MONTHLY_FEE = "ServiceCMinimumMonthlyFee"
    SERVICE_C_OTHER = "ServiceCOther"

    def visit(
        self,
        other: typing.Callable[[], T_Result],
        service_c_account_fee: typing.Callable[[], T_Result],
        service_c_account_fee_monthly: typing.Callable[[], T_Result],
        service_c_account_fee_quarterly: typing.Callable[[], T_Result],
        service_c_fixed_tariff: typing.Callable[[], T_Result],
        service_c_busi_dep_acc_breakage: typing.Callable[[], T_Result],
        service_c_minimum_monthly_fee: typing.Callable[[], T_Result],
        service_c_other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem.OTHER:
            return other()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem.SERVICE_C_ACCOUNT_FEE:
            return service_c_account_fee()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem.SERVICE_C_ACCOUNT_FEE_MONTHLY:
            return service_c_account_fee_monthly()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem.SERVICE_C_ACCOUNT_FEE_QUARTERLY:
            return service_c_account_fee_quarterly()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem.SERVICE_C_FIXED_TARIFF:
            return service_c_fixed_tariff()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem.SERVICE_C_BUSI_DEP_ACC_BREAKAGE:
            return service_c_busi_dep_acc_breakage()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem.SERVICE_C_MINIMUM_MONTHLY_FEE:
            return service_c_minimum_monthly_fee()
        if self is ObbcaData1OtherFeesChargesItemFeeChargeCapItemFeeTypeItem.SERVICE_C_OTHER:
            return service_c_other()
