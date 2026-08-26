

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataTableColumnType(enum.StrEnum):
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    GEOMETRY = "geometry"
    INTEGER = "integer"
    NUMBER = "number"
    STRING = "string"
    TIME = "time"
    UNKNOWN = "unknown"

    def visit(
        self,
        boolean: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        datetime: typing.Callable[[], T_Result],
        geometry: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        string: typing.Callable[[], T_Result],
        time: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataTableColumnType.BOOLEAN:
            return boolean()
        if self is DataTableColumnType.DATE:
            return date()
        if self is DataTableColumnType.DATETIME:
            return datetime()
        if self is DataTableColumnType.GEOMETRY:
            return geometry()
        if self is DataTableColumnType.INTEGER:
            return integer()
        if self is DataTableColumnType.NUMBER:
            return number()
        if self is DataTableColumnType.STRING:
            return string()
        if self is DataTableColumnType.TIME:
            return time()
        if self is DataTableColumnType.UNKNOWN:
            return unknown()
