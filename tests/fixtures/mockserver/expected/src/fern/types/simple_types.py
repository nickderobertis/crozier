

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleTypes(enum.StrEnum):
    ARRAY = "array"
    BOOLEAN = "boolean"
    INTEGER = "integer"
    NULL = "null"
    NUMBER = "number"
    OBJECT = "object"
    STRING = "string"

    def visit(
        self,
        array: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        object: typing.Callable[[], T_Result],
        string: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SimpleTypes.ARRAY:
            return array()
        if self is SimpleTypes.BOOLEAN:
            return boolean()
        if self is SimpleTypes.INTEGER:
            return integer()
        if self is SimpleTypes.NULL:
            return null()
        if self is SimpleTypes.NUMBER:
            return number()
        if self is SimpleTypes.OBJECT:
            return object()
        if self is SimpleTypes.STRING:
            return string()
