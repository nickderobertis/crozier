

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationResultOutcome(enum.StrEnum):
    AUTHENTICATED = "authenticated"
    FAILED = "failed"
    UNAVAILABLE = "unavailable"
    REJECTED = "rejected"
    ATTEMPT = "attempt"

    def visit(
        self,
        authenticated: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
        rejected: typing.Callable[[], T_Result],
        attempt: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuthenticationResultOutcome.AUTHENTICATED:
            return authenticated()
        if self is AuthenticationResultOutcome.FAILED:
            return failed()
        if self is AuthenticationResultOutcome.UNAVAILABLE:
            return unavailable()
        if self is AuthenticationResultOutcome.REJECTED:
            return rejected()
        if self is AuthenticationResultOutcome.ATTEMPT:
            return attempt()
