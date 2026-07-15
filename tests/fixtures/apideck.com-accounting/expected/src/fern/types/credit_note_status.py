

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CreditNoteStatus(str, enum.Enum):
    """
    Status of credit notes
    """

    DRAFT = "draft"
    AUTHORISED = "authorised"
    PAID = "paid"
    VOIDED = "voided"
    DELETED = "deleted"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        authorised: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        voided: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditNoteStatus.DRAFT:
            return draft()
        if self is CreditNoteStatus.AUTHORISED:
            return authorised()
        if self is CreditNoteStatus.PAID:
            return paid()
        if self is CreditNoteStatus.VOIDED:
            return voided()
        if self is CreditNoteStatus.DELETED:
            return deleted()
