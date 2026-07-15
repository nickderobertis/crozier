

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PaymentStatus(str, enum.Enum):
    """
    Status of payment
    """

    AUTHORISED = "authorised"
    PAID = "paid"
    VOIDED = "voided"
    DELETED = "deleted"

    def visit(
        self,
        authorised: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        voided: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentStatus.AUTHORISED:
            return authorised()
        if self is PaymentStatus.PAID:
            return paid()
        if self is PaymentStatus.VOIDED:
            return voided()
        if self is PaymentStatus.DELETED:
            return deleted()
