

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PricebookTypeOne(enum.StrEnum):
    NON_STANDARD = "Non-Standard"

    def visit(self, non_standard: typing.Callable[[], T_Result]) -> T_Result:
        if self is PricebookTypeOne.NON_STANDARD:
            return non_standard()
