

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UiFilterModelOperator(enum.StrEnum):
    """
    Operator
    """

    EQUAL_TO = "="

    def visit(self, equal_to: typing.Callable[[], T_Result]) -> T_Result:
        if self is UiFilterModelOperator.EQUAL_TO:
            return equal_to()
