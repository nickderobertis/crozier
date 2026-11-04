

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTransactionsV21RequestTypesItem(enum.StrEnum):
    PAYMENT = "PAYMENT"
    REFUND = "REFUND"
    CHARGE_BACK = "CHARGE_BACK"

    def visit(
        self,
        payment: typing.Callable[[], T_Result],
        refund: typing.Callable[[], T_Result],
        charge_back: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListTransactionsV21RequestTypesItem.PAYMENT:
            return payment()
        if self is ListTransactionsV21RequestTypesItem.REFUND:
            return refund()
        if self is ListTransactionsV21RequestTypesItem.CHARGE_BACK:
            return charge_back()
