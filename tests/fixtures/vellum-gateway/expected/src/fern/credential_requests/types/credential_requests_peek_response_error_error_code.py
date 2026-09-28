

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CredentialRequestsPeekResponseErrorErrorCode(enum.StrEnum):
    INVALID = "INVALID"
    EXPIRED = "EXPIRED"
    USED = "USED"

    def visit(
        self,
        invalid: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        used: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CredentialRequestsPeekResponseErrorErrorCode.INVALID:
            return invalid()
        if self is CredentialRequestsPeekResponseErrorErrorCode.EXPIRED:
            return expired()
        if self is CredentialRequestsPeekResponseErrorErrorCode.USED:
            return used()
