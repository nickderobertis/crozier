

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentificationStatusResponseStatus(enum.StrEnum):
    VALID = "valid"
    EXPIRED = "expired"
    REVOKED = "revoked"
    PENDING = "pending"

    def visit(
        self,
        valid: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        revoked: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentificationStatusResponseStatus.VALID:
            return valid()
        if self is IdentificationStatusResponseStatus.EXPIRED:
            return expired()
        if self is IdentificationStatusResponseStatus.REVOKED:
            return revoked()
        if self is IdentificationStatusResponseStatus.PENDING:
            return pending()
