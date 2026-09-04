

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SignatureStatusStatus(enum.StrEnum):
    PENDING = "pending"
    SIGNED = "signed"
    EXPIRED = "expired"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        signed: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SignatureStatusStatus.PENDING:
            return pending()
        if self is SignatureStatusStatus.SIGNED:
            return signed()
        if self is SignatureStatusStatus.EXPIRED:
            return expired()
        if self is SignatureStatusStatus.FAILED:
            return failed()
