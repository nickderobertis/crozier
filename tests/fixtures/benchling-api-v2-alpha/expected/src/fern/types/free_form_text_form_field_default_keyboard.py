

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FreeFormTextFormFieldDefaultKeyboard(enum.StrEnum):
    NUMERIC = "NUMERIC"
    DEFAULT = "DEFAULT"

    def visit(self, numeric: typing.Callable[[], T_Result], default: typing.Callable[[], T_Result]) -> T_Result:
        if self is FreeFormTextFormFieldDefaultKeyboard.NUMERIC:
            return numeric()
        if self is FreeFormTextFormFieldDefaultKeyboard.DEFAULT:
            return default()
