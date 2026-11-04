

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActActionResponseStatus(enum.StrEnum):
    COMPLETED = "completed"
    RUNNING = "running"
    AWAITING_USER = "awaiting_user"
    APPROVAL_REQUIRED = "approval_required"
    AUTHENTICATION_REQUIRED = "authentication_required"
    CONNECTION_REQUIRED = "connection_required"
    PAYMENT_REQUIRED = "payment_required"
    VERIFICATION_REQUIRED = "verification_required"
    INSUFFICIENT_AUTHORITY = "insufficient_authority"
    PROVIDER_UNAVAILABLE = "provider_unavailable"
    STOPPED = "stopped"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        awaiting_user: typing.Callable[[], T_Result],
        approval_required: typing.Callable[[], T_Result],
        authentication_required: typing.Callable[[], T_Result],
        connection_required: typing.Callable[[], T_Result],
        payment_required: typing.Callable[[], T_Result],
        verification_required: typing.Callable[[], T_Result],
        insufficient_authority: typing.Callable[[], T_Result],
        provider_unavailable: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActActionResponseStatus.COMPLETED:
            return completed()
        if self is ActActionResponseStatus.RUNNING:
            return running()
        if self is ActActionResponseStatus.AWAITING_USER:
            return awaiting_user()
        if self is ActActionResponseStatus.APPROVAL_REQUIRED:
            return approval_required()
        if self is ActActionResponseStatus.AUTHENTICATION_REQUIRED:
            return authentication_required()
        if self is ActActionResponseStatus.CONNECTION_REQUIRED:
            return connection_required()
        if self is ActActionResponseStatus.PAYMENT_REQUIRED:
            return payment_required()
        if self is ActActionResponseStatus.VERIFICATION_REQUIRED:
            return verification_required()
        if self is ActActionResponseStatus.INSUFFICIENT_AUTHORITY:
            return insufficient_authority()
        if self is ActActionResponseStatus.PROVIDER_UNAVAILABLE:
            return provider_unavailable()
        if self is ActActionResponseStatus.STOPPED:
            return stopped()
