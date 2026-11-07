

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryableType(enum.StrEnum):
    """
    the property type
    """

    STRING = "string"
    URI = "uri"
    NUMBER = "number"
    INTEGER = "integer"
    DATE = "date"
    DATE_TIME = "dateTime"
    BOOLEAN = "boolean"
    GEOMETRY = "geometry"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        uri: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        date_time: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        geometry: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QueryableType.STRING:
            return string()
        if self is QueryableType.URI:
            return uri()
        if self is QueryableType.NUMBER:
            return number()
        if self is QueryableType.INTEGER:
            return integer()
        if self is QueryableType.DATE:
            return date()
        if self is QueryableType.DATE_TIME:
            return date_time()
        if self is QueryableType.BOOLEAN:
            return boolean()
        if self is QueryableType.GEOMETRY:
            return geometry()
