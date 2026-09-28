

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TitlerDisabledErrorError(enum.StrEnum):
    TITLER_DISABLED = "titler_disabled"

    def visit(self, titler_disabled: typing.Callable[[], T_Result]) -> T_Result:
        if self is TitlerDisabledErrorError.TITLER_DISABLED:
            return titler_disabled()
