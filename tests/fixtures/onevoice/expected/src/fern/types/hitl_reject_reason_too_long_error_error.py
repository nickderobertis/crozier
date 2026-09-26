

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HitlRejectReasonTooLongErrorError(enum.StrEnum):
    REJECT_REASON_TOO_LONG = "reject_reason too long"

    def visit(self, reject_reason_too_long: typing.Callable[[], T_Result]) -> T_Result:
        if self is HitlRejectReasonTooLongErrorError.REJECT_REASON_TOO_LONG:
            return reject_reason_too_long()
