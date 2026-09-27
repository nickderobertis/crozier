

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetPaymentsIdV3RequestFieldsItem(enum.StrEnum):
    PAYMENT_ID = "payment_id"
    TRANSACTION_ID = "transaction_id"
    SCHOOL_ID = "school_id"
    FAMILY_ID = "family_id"
    FAMILY_NAME = "family_name"
    TRANSACTION_DATE = "transaction_date"
    AMOUNT = "amount"
    FEE_AMOUNT = "fee_amount"
    TOTAL_AMOUNT = "total_amount"
    BALANCE = "balance"
    STATE = "state"
    RECEIPT_NUMBER = "receipt_number"
    PAYMENT_MODE = "payment_mode"
    PAYMENT_METHOD_SUB_KIND = "payment_method_sub_kind"
    DESCRIPTION = "description"
    IS_POSTED = "is_posted"
    PAYD_ONLINE = "payd_online"
    AUTO_BILLING = "auto_billing"
    CREATED_AT = "created_at"

    def visit(
        self,
        payment_id: typing.Callable[[], T_Result],
        transaction_id: typing.Callable[[], T_Result],
        school_id: typing.Callable[[], T_Result],
        family_id: typing.Callable[[], T_Result],
        family_name: typing.Callable[[], T_Result],
        transaction_date: typing.Callable[[], T_Result],
        amount: typing.Callable[[], T_Result],
        fee_amount: typing.Callable[[], T_Result],
        total_amount: typing.Callable[[], T_Result],
        balance: typing.Callable[[], T_Result],
        state: typing.Callable[[], T_Result],
        receipt_number: typing.Callable[[], T_Result],
        payment_mode: typing.Callable[[], T_Result],
        payment_method_sub_kind: typing.Callable[[], T_Result],
        description: typing.Callable[[], T_Result],
        is_posted: typing.Callable[[], T_Result],
        payd_online: typing.Callable[[], T_Result],
        auto_billing: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetPaymentsIdV3RequestFieldsItem.PAYMENT_ID:
            return payment_id()
        if self is GetPaymentsIdV3RequestFieldsItem.TRANSACTION_ID:
            return transaction_id()
        if self is GetPaymentsIdV3RequestFieldsItem.SCHOOL_ID:
            return school_id()
        if self is GetPaymentsIdV3RequestFieldsItem.FAMILY_ID:
            return family_id()
        if self is GetPaymentsIdV3RequestFieldsItem.FAMILY_NAME:
            return family_name()
        if self is GetPaymentsIdV3RequestFieldsItem.TRANSACTION_DATE:
            return transaction_date()
        if self is GetPaymentsIdV3RequestFieldsItem.AMOUNT:
            return amount()
        if self is GetPaymentsIdV3RequestFieldsItem.FEE_AMOUNT:
            return fee_amount()
        if self is GetPaymentsIdV3RequestFieldsItem.TOTAL_AMOUNT:
            return total_amount()
        if self is GetPaymentsIdV3RequestFieldsItem.BALANCE:
            return balance()
        if self is GetPaymentsIdV3RequestFieldsItem.STATE:
            return state()
        if self is GetPaymentsIdV3RequestFieldsItem.RECEIPT_NUMBER:
            return receipt_number()
        if self is GetPaymentsIdV3RequestFieldsItem.PAYMENT_MODE:
            return payment_mode()
        if self is GetPaymentsIdV3RequestFieldsItem.PAYMENT_METHOD_SUB_KIND:
            return payment_method_sub_kind()
        if self is GetPaymentsIdV3RequestFieldsItem.DESCRIPTION:
            return description()
        if self is GetPaymentsIdV3RequestFieldsItem.IS_POSTED:
            return is_posted()
        if self is GetPaymentsIdV3RequestFieldsItem.PAYD_ONLINE:
            return payd_online()
        if self is GetPaymentsIdV3RequestFieldsItem.AUTO_BILLING:
            return auto_billing()
        if self is GetPaymentsIdV3RequestFieldsItem.CREATED_AT:
            return created_at()
