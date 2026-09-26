

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HitlExpiredErrorError(enum.StrEnum):
    APPROVAL_EXPIRED = "approval_expired"

    def visit(self, approval_expired: typing.Callable[[], T_Result]) -> T_Result:
        if self is HitlExpiredErrorError.APPROVAL_EXPIRED:
            return approval_expired()
