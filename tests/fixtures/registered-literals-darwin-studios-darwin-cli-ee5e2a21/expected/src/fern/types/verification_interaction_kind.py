

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VerificationInteractionKind(enum.StrEnum):
    VERIFICATION = "verification"

    def visit(self, verification: typing.Callable[[], T_Result]) -> T_Result:
        if self is VerificationInteractionKind.VERIFICATION:
            return verification()
