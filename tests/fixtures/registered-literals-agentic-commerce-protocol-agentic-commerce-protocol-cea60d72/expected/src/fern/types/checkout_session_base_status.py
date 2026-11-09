

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CheckoutSessionBaseStatus(enum.StrEnum):
    NOT_READY_FOR_PAYMENT = "not_ready_for_payment"
    READY_FOR_PAYMENT = "ready_for_payment"
    COMPLETED = "completed"
    CANCELED = "canceled"
    IN_PROGRESS = "in_progress"
    AUTHENTICATION_REQUIRED = "authentication_required"

    def visit(
        self,
        not_ready_for_payment: typing.Callable[[], T_Result],
        ready_for_payment: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        authentication_required: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CheckoutSessionBaseStatus.NOT_READY_FOR_PAYMENT:
            return not_ready_for_payment()
        if self is CheckoutSessionBaseStatus.READY_FOR_PAYMENT:
            return ready_for_payment()
        if self is CheckoutSessionBaseStatus.COMPLETED:
            return completed()
        if self is CheckoutSessionBaseStatus.CANCELED:
            return canceled()
        if self is CheckoutSessionBaseStatus.IN_PROGRESS:
            return in_progress()
        if self is CheckoutSessionBaseStatus.AUTHENTICATION_REQUIRED:
            return authentication_required()
