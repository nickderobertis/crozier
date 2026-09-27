

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFamilyBalancesV3RequestFieldsItem(enum.StrEnum):
    FAMILY_ID = "family_id"
    SCHOOL_ID = "school_id"
    FAMILY_NAME = "family_name"
    FAMILY_STUDENT_COUNT = "family_student_count"
    TRANSACTION_ID = "transaction_id"
    TRANSACTION_DATE = "transaction_date"
    AMOUNT = "amount"
    BALANCE = "balance"
    RECEIPT_NUMBER = "receipt_number"
    KIND = "kind"

    def visit(
        self,
        family_id: typing.Callable[[], T_Result],
        school_id: typing.Callable[[], T_Result],
        family_name: typing.Callable[[], T_Result],
        family_student_count: typing.Callable[[], T_Result],
        transaction_id: typing.Callable[[], T_Result],
        transaction_date: typing.Callable[[], T_Result],
        amount: typing.Callable[[], T_Result],
        balance: typing.Callable[[], T_Result],
        receipt_number: typing.Callable[[], T_Result],
        kind: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetFamilyBalancesV3RequestFieldsItem.FAMILY_ID:
            return family_id()
        if self is GetFamilyBalancesV3RequestFieldsItem.SCHOOL_ID:
            return school_id()
        if self is GetFamilyBalancesV3RequestFieldsItem.FAMILY_NAME:
            return family_name()
        if self is GetFamilyBalancesV3RequestFieldsItem.FAMILY_STUDENT_COUNT:
            return family_student_count()
        if self is GetFamilyBalancesV3RequestFieldsItem.TRANSACTION_ID:
            return transaction_id()
        if self is GetFamilyBalancesV3RequestFieldsItem.TRANSACTION_DATE:
            return transaction_date()
        if self is GetFamilyBalancesV3RequestFieldsItem.AMOUNT:
            return amount()
        if self is GetFamilyBalancesV3RequestFieldsItem.BALANCE:
            return balance()
        if self is GetFamilyBalancesV3RequestFieldsItem.RECEIPT_NUMBER:
            return receipt_number()
        if self is GetFamilyBalancesV3RequestFieldsItem.KIND:
            return kind()
