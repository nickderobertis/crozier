

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DetailedCustomerInvoiceTypeOne(enum.StrEnum):
    TO_BE_APPROVED = "toBeApproved"

    def visit(self, to_be_approved: typing.Callable[[], T_Result]) -> T_Result:
        if self is DetailedCustomerInvoiceTypeOne.TO_BE_APPROVED:
            return to_be_approved()
