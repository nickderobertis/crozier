

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SandboxItemSetVerificationStatusRequestVerificationStatus(enum.StrEnum):
    """
    The verification status to set the account to.
    """

    AUTOMATICALLY_VERIFIED = "automatically_verified"
    VERIFICATION_EXPIRED = "verification_expired"

    def visit(
        self, automatically_verified: typing.Callable[[], T_Result], verification_expired: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is SandboxItemSetVerificationStatusRequestVerificationStatus.AUTOMATICALLY_VERIFIED:
            return automatically_verified()
        if self is SandboxItemSetVerificationStatusRequestVerificationStatus.VERIFICATION_EXPIRED:
            return verification_expired()
