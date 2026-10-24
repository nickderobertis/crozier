

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataTypeResult(enum.StrEnum):
    """
    the result type.
    """

    VOID = "void"
    STRING = "string"
    NUMBER = "number"
    DATE = "date"
    TIME = "time"
    DATETIME = "datetime"

    def visit(
        self,
        void: typing.Callable[[], T_Result],
        string: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        time: typing.Callable[[], T_Result],
        datetime: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataTypeResult.VOID:
            return void()
        if self is DataTypeResult.STRING:
            return string()
        if self is DataTypeResult.NUMBER:
            return number()
        if self is DataTypeResult.DATE:
            return date()
        if self is DataTypeResult.TIME:
            return time()
        if self is DataTypeResult.DATETIME:
            return datetime()
