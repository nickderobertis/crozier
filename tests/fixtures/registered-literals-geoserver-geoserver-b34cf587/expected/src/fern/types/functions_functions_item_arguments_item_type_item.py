

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FunctionsFunctionsItemArgumentsItemTypeItem(enum.StrEnum):
    STRING = "string"
    NUMBER = "number"
    INTEGER = "integer"
    DATETIME = "datetime"
    GEOMETRY = "geometry"
    BOOLEAN = "boolean"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        datetime: typing.Callable[[], T_Result],
        geometry: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FunctionsFunctionsItemArgumentsItemTypeItem.STRING:
            return string()
        if self is FunctionsFunctionsItemArgumentsItemTypeItem.NUMBER:
            return number()
        if self is FunctionsFunctionsItemArgumentsItemTypeItem.INTEGER:
            return integer()
        if self is FunctionsFunctionsItemArgumentsItemTypeItem.DATETIME:
            return datetime()
        if self is FunctionsFunctionsItemArgumentsItemTypeItem.GEOMETRY:
            return geometry()
        if self is FunctionsFunctionsItemArgumentsItemTypeItem.BOOLEAN:
            return boolean()
