

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SchemaPropertyType(enum.StrEnum):
    STRING = "string"
    NUMBER = "number"
    BOOLEAN = "boolean"
    ARRAY = "array"
    OBJECT = "object"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        array: typing.Callable[[], T_Result],
        object: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SchemaPropertyType.STRING:
            return string()
        if self is SchemaPropertyType.NUMBER:
            return number()
        if self is SchemaPropertyType.BOOLEAN:
            return boolean()
        if self is SchemaPropertyType.ARRAY:
            return array()
        if self is SchemaPropertyType.OBJECT:
            return object()
