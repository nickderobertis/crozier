

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CalculatedFieldType(enum.StrEnum):
    """
    Choose whether the value will be text or a numeric value (number).
    """

    NUMBER = "NUMBER"
    TEXT = "TEXT"

    def visit(self, number: typing.Callable[[], T_Result], text: typing.Callable[[], T_Result]) -> T_Result:
        if self is CalculatedFieldType.NUMBER:
            return number()
        if self is CalculatedFieldType.TEXT:
            return text()
