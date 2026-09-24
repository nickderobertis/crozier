

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PricebookTypeTwo(enum.StrEnum):
    CUSTOM = "Custom"

    def visit(self, custom: typing.Callable[[], T_Result]) -> T_Result:
        if self is PricebookTypeTwo.CUSTOM:
            return custom()
