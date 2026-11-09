

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationResultOutcome(enum.StrEnum):
    """
    The outcome of this 3DS Authentication.
    """

    ABANDONED = "abandoned"
    ATTEMPT_ACKNOWLEDGED = "attempt_acknowledged"
    AUTHENTICATED = "authenticated"
    CANCELED = "canceled"
    DENIED = "denied"
    INFORMATIONAL = "informational"
    INTERNAL_ERROR = "internal_error"
    NOT_SUPPORTED = "not_supported"
    PROCESSING_ERROR = "processing_error"
    REJECTED = "rejected"

    def visit(
        self,
        abandoned: typing.Callable[[], T_Result],
        attempt_acknowledged: typing.Callable[[], T_Result],
        authenticated: typing.Callable[[], T_Result],
        canceled: typing.Callable[[], T_Result],
        denied: typing.Callable[[], T_Result],
        informational: typing.Callable[[], T_Result],
        internal_error: typing.Callable[[], T_Result],
        not_supported: typing.Callable[[], T_Result],
        processing_error: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthenticationResultOutcome.ABANDONED:
            return abandoned()
        if self is AuthenticationResultOutcome.ATTEMPT_ACKNOWLEDGED:
            return attempt_acknowledged()
        if self is AuthenticationResultOutcome.AUTHENTICATED:
            return authenticated()
        if self is AuthenticationResultOutcome.CANCELED:
            return canceled()
        if self is AuthenticationResultOutcome.DENIED:
            return denied()
        if self is AuthenticationResultOutcome.INFORMATIONAL:
            return informational()
        if self is AuthenticationResultOutcome.INTERNAL_ERROR:
            return internal_error()
        if self is AuthenticationResultOutcome.NOT_SUPPORTED:
            return not_supported()
        if self is AuthenticationResultOutcome.PROCESSING_ERROR:
            return processing_error()
        if self is AuthenticationResultOutcome.REJECTED:
            return rejected()
