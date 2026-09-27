

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConsentRequiredResponseCode(enum.StrEnum):
    CONSENT_REQUIRED = "consent_required"

    def visit(self, consent_required: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConsentRequiredResponseCode.CONSENT_REQUIRED:
            return consent_required()
