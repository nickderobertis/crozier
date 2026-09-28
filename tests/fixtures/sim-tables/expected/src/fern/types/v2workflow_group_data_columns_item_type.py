

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2WorkflowGroupDataColumnsItemType(enum.StrEnum):
    """
    Data type of values stored in the column.
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
        if self is V2WorkflowGroupDataColumnsItemType.STRING:
            return string()
        if self is V2WorkflowGroupDataColumnsItemType.NUMBER:
            return number()
        if self is V2WorkflowGroupDataColumnsItemType.CURRENCY:
            return currency()
        if self is V2WorkflowGroupDataColumnsItemType.BOOLEAN:
            return boolean()
        if self is V2WorkflowGroupDataColumnsItemType.DATE:
            return date()
        if self is V2WorkflowGroupDataColumnsItemType.JSON:
            return json()
        if self is V2WorkflowGroupDataColumnsItemType.SELECT:
            return select()
