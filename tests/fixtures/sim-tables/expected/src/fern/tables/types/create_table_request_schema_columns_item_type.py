

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateTableRequestSchemaColumnsItemType(enum.StrEnum):
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
        if self is CreateTableRequestSchemaColumnsItemType.STRING:
            return string()
        if self is CreateTableRequestSchemaColumnsItemType.NUMBER:
            return number()
        if self is CreateTableRequestSchemaColumnsItemType.CURRENCY:
            return currency()
        if self is CreateTableRequestSchemaColumnsItemType.BOOLEAN:
            return boolean()
        if self is CreateTableRequestSchemaColumnsItemType.DATE:
            return date()
        if self is CreateTableRequestSchemaColumnsItemType.JSON:
            return json()
        if self is CreateTableRequestSchemaColumnsItemType.SELECT:
            return select()
