

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetCustomerInvoicesRequestSortField(enum.StrEnum):
    ID = "id"
    CREATED_AT = "createdAt"
    DUE_DATE = "dueDate"

    def visit(
        self,
        id: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        due_date: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetCustomerInvoicesRequestSortField.ID:
            return id()
        if self is GetCustomerInvoicesRequestSortField.CREATED_AT:
            return created_at()
        if self is GetCustomerInvoicesRequestSortField.DUE_DATE:
            return due_date()
