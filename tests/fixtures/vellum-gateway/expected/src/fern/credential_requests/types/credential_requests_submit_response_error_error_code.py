

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CredentialRequestsSubmitResponseErrorErrorCode(enum.StrEnum):
    INVALID = "INVALID"
    EXPIRED = "EXPIRED"
    USED = "USED"

    def visit(
        self,
        invalid: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        used: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CredentialRequestsSubmitResponseErrorErrorCode.INVALID:
            return invalid()
        if self is CredentialRequestsSubmitResponseErrorErrorCode.EXPIRED:
            return expired()
        if self is CredentialRequestsSubmitResponseErrorErrorCode.USED:
            return used()
