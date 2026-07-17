

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataType(enum.StrEnum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    OBJECT = "object"
    ARRAY = "array"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        object: typing.Callable[[], T_Result],
        array: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataType.STRING:
            return string()
        if self is DataType.NUMBER:
            return number()
        if self is DataType.BOOLEAN:
            return boolean()
        if self is DataType.OBJECT:
            return object()
        if self is DataType.ARRAY:
            return array()
