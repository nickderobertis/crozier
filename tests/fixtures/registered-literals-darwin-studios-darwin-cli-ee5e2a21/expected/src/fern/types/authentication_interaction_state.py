

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationInteractionState(enum.StrEnum):
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
        if self is AuthenticationInteractionState.REQUIRED:
            return required()
        if self is AuthenticationInteractionState.PENDING:
            return pending()
        if self is AuthenticationInteractionState.COMPLETE:
            return complete()
        if self is AuthenticationInteractionState.DECLINED:
            return declined()
        if self is AuthenticationInteractionState.EXPIRED:
            return expired()
        if self is AuthenticationInteractionState.FAILED:
            return failed()
