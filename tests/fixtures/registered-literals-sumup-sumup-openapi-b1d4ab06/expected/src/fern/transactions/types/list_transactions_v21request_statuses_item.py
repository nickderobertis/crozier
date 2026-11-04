

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTransactionsV21RequestStatusesItem(enum.StrEnum):
    SUCCESSFUL = "SUCCESSFUL"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"
    CHARGE_BACK = "CHARGE_BACK"

    def visit(
        self,
        successful: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        refunded: typing.Callable[[], T_Result],
        charge_back: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListTransactionsV21RequestStatusesItem.SUCCESSFUL:
            return successful()
        if self is ListTransactionsV21RequestStatusesItem.CANCELLED:
            return cancelled()
        if self is ListTransactionsV21RequestStatusesItem.FAILED:
            return failed()
        if self is ListTransactionsV21RequestStatusesItem.REFUNDED:
            return refunded()
        if self is ListTransactionsV21RequestStatusesItem.CHARGE_BACK:
            return charge_back()
