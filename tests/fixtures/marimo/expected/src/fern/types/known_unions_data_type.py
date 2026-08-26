

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KnownUnionsDataType(enum.StrEnum):
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
        if self is KnownUnionsDataType.BOOLEAN:
            return boolean()
        if self is KnownUnionsDataType.DATE:
            return date()
        if self is KnownUnionsDataType.DATETIME:
            return datetime()
        if self is KnownUnionsDataType.GEOMETRY:
            return geometry()
        if self is KnownUnionsDataType.INTEGER:
            return integer()
        if self is KnownUnionsDataType.NUMBER:
            return number()
        if self is KnownUnionsDataType.STRING:
            return string()
        if self is KnownUnionsDataType.TIME:
            return time()
        if self is KnownUnionsDataType.UNKNOWN:
            return unknown()
