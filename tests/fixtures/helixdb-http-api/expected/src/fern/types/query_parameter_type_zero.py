

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryParameterTypeZero(enum.StrEnum):
    BOOL = "bool"
    I64 = "i64"
    STRING = "string"
    DATE_TIME = "date_time"
    VALUE = "value"
    OBJECT = "object"

    def visit(
        self,
        bool_: typing.Callable[[], T_Result],
        i64: typing.Callable[[], T_Result],
        string: typing.Callable[[], T_Result],
        date_time: typing.Callable[[], T_Result],
        value: typing.Callable[[], T_Result],
        object: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QueryParameterTypeZero.BOOL:
            return bool_()
        if self is QueryParameterTypeZero.I64:
            return i64()
        if self is QueryParameterTypeZero.STRING:
            return string()
        if self is QueryParameterTypeZero.DATE_TIME:
            return date_time()
        if self is QueryParameterTypeZero.VALUE:
            return value()
        if self is QueryParameterTypeZero.OBJECT:
            return object()
