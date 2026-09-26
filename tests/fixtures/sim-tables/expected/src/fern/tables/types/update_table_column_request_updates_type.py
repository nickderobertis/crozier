

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateTableColumnRequestUpdatesType(enum.StrEnum):
    """
    Replacement column data type.
    """

    STRING = "string"
    NUMBER = "number"
    CURRENCY = "currency"
    BOOLEAN = "boolean"
    DATE = "date"
    JSON = "json"
    SELECT = "select"

    def visit(
        self,
        string: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        currency: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        select: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateTableColumnRequestUpdatesType.STRING:
            return string()
        if self is UpdateTableColumnRequestUpdatesType.NUMBER:
            return number()
        if self is UpdateTableColumnRequestUpdatesType.CURRENCY:
            return currency()
        if self is UpdateTableColumnRequestUpdatesType.BOOLEAN:
            return boolean()
        if self is UpdateTableColumnRequestUpdatesType.DATE:
            return date()
        if self is UpdateTableColumnRequestUpdatesType.JSON:
            return json()
        if self is UpdateTableColumnRequestUpdatesType.SELECT:
            return select()
