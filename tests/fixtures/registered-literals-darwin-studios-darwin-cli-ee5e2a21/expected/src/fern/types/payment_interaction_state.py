

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PaymentInteractionState(enum.StrEnum):
    REQUIRED = "required"
    PENDING = "pending"
    COMPLETE = "complete"
    DECLINED = "declined"
    EXPIRED = "expired"
    FAILED = "failed"

    def visit(
        self,
        required: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
        declined: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentInteractionState.REQUIRED:
            return required()
        if self is PaymentInteractionState.PENDING:
            return pending()
        if self is PaymentInteractionState.COMPLETE:
            return complete()
        if self is PaymentInteractionState.DECLINED:
            return declined()
        if self is PaymentInteractionState.EXPIRED:
            return expired()
        if self is PaymentInteractionState.FAILED:
            return failed()
