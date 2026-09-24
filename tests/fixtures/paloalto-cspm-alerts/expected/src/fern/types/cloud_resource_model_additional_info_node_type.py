

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CloudResourceModelAdditionalInfoNodeType(enum.StrEnum):
    ARRAY = "ARRAY"
    BINARY = "BINARY"
    BOOLEAN = "BOOLEAN"
    MISSING = "MISSING"
    NULL = "NULL"
    NUMBER = "NUMBER"
    OBJECT = "OBJECT"
    POJO = "POJO"
    STRING = "STRING"

    def visit(
        self,
        array: typing.Callable[[], T_Result],
        binary: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        missing: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        object: typing.Callable[[], T_Result],
        pojo: typing.Callable[[], T_Result],
        string: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CloudResourceModelAdditionalInfoNodeType.ARRAY:
            return array()
        if self is CloudResourceModelAdditionalInfoNodeType.BINARY:
            return binary()
        if self is CloudResourceModelAdditionalInfoNodeType.BOOLEAN:
            return boolean()
        if self is CloudResourceModelAdditionalInfoNodeType.MISSING:
            return missing()
        if self is CloudResourceModelAdditionalInfoNodeType.NULL:
            return null()
        if self is CloudResourceModelAdditionalInfoNodeType.NUMBER:
            return number()
        if self is CloudResourceModelAdditionalInfoNodeType.OBJECT:
            return object()
        if self is CloudResourceModelAdditionalInfoNodeType.POJO:
            return pojo()
        if self is CloudResourceModelAdditionalInfoNodeType.STRING:
            return string()
