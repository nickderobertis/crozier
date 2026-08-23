

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataType(enum.StrEnum):
    BOOLEAN = "boolean"
    INTEGER = "integer"
    NUMBER = "number"
    STRING = "string"
    ARRAY = "array"
    OBJECT = "object"

    def visit(
        self,
        boolean: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        string: typing.Callable[[], T_Result],
        array: typing.Callable[[], T_Result],
        object: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataType.BOOLEAN:
            return boolean()
        if self is DataType.INTEGER:
            return integer()
        if self is DataType.NUMBER:
            return number()
        if self is DataType.STRING:
            return string()
        if self is DataType.ARRAY:
            return array()
        if self is DataType.OBJECT:
            return object()
