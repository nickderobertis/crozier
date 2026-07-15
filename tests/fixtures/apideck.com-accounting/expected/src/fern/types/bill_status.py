

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BillStatus(str, enum.Enum):
    """
    Invoice status
    """

    DRAFT = "draft"
    SUBMITTED = "submitted"
    AUTHORISED = "authorised"
    PARTIALLY_PAID = "partially_paid"
    PAID = "paid"
    VOID = "void"
    CREDIT = "credit"
    DELETED = "deleted"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        submitted: typing.Callable[[], T_Result],
        authorised: typing.Callable[[], T_Result],
        partially_paid: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        void: typing.Callable[[], T_Result],
        credit: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BillStatus.DRAFT:
            return draft()
        if self is BillStatus.SUBMITTED:
            return submitted()
        if self is BillStatus.AUTHORISED:
            return authorised()
        if self is BillStatus.PARTIALLY_PAID:
            return partially_paid()
        if self is BillStatus.PAID:
            return paid()
        if self is BillStatus.VOID:
            return void()
        if self is BillStatus.CREDIT:
            return credit()
        if self is BillStatus.DELETED:
            return deleted()
