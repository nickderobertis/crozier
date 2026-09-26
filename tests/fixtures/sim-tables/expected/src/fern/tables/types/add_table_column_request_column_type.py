

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AddTableColumnRequestColumnType(enum.StrEnum):
    """
    Column data type.
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
        if self is AddTableColumnRequestColumnType.STRING:
            return string()
        if self is AddTableColumnRequestColumnType.NUMBER:
            return number()
        if self is AddTableColumnRequestColumnType.CURRENCY:
            return currency()
        if self is AddTableColumnRequestColumnType.BOOLEAN:
            return boolean()
        if self is AddTableColumnRequestColumnType.DATE:
            return date()
        if self is AddTableColumnRequestColumnType.JSON:
            return json()
        if self is AddTableColumnRequestColumnType.SELECT:
            return select()
