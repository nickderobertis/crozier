

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FreeFormTextFormFieldCannedResponsesBehavior(enum.StrEnum):
    ADDITIVE = "ADDITIVE"
    REPLACE = "REPLACE"

    def visit(self, additive: typing.Callable[[], T_Result], replace: typing.Callable[[], T_Result]) -> T_Result:
        if self is FreeFormTextFormFieldCannedResponsesBehavior.ADDITIVE:
            return additive()
        if self is FreeFormTextFormFieldCannedResponsesBehavior.REPLACE:
            return replace()
