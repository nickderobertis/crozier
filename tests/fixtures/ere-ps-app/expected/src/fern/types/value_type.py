

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValueType(enum.StrEnum):
    ARRAY = "ARRAY"
    OBJECT = "OBJECT"
    STRING = "STRING"
    NUMBER = "NUMBER"
    TRUE = "TRUE"
    FALSE = "FALSE"
    NULL = "NULL"

    def visit(
        self,
        array: typing.Callable[[], T_Result],
        object: typing.Callable[[], T_Result],
        string: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        true: typing.Callable[[], T_Result],
        false: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValueType.ARRAY:
            return array()
        if self is ValueType.OBJECT:
            return object()
        if self is ValueType.STRING:
            return string()
        if self is ValueType.NUMBER:
            return number()
        if self is ValueType.TRUE:
            return true()
        if self is ValueType.FALSE:
            return false()
        if self is ValueType.NULL:
            return null()
