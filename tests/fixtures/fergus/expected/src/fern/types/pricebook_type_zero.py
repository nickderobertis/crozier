

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PricebookTypeZero(enum.StrEnum):
    STANDARD = "Standard"

    def visit(self, standard: typing.Callable[[], T_Result]) -> T_Result:
        if self is PricebookTypeZero.STANDARD:
            return standard()
