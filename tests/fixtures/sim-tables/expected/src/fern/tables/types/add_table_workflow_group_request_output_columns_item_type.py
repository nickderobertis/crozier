

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AddTableWorkflowGroupRequestOutputColumnsItemType(enum.StrEnum):
    """
    Output column data type.
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
        if self is AddTableWorkflowGroupRequestOutputColumnsItemType.STRING:
            return string()
        if self is AddTableWorkflowGroupRequestOutputColumnsItemType.NUMBER:
            return number()
        if self is AddTableWorkflowGroupRequestOutputColumnsItemType.CURRENCY:
            return currency()
        if self is AddTableWorkflowGroupRequestOutputColumnsItemType.BOOLEAN:
            return boolean()
        if self is AddTableWorkflowGroupRequestOutputColumnsItemType.DATE:
            return date()
        if self is AddTableWorkflowGroupRequestOutputColumnsItemType.JSON:
            return json()
        if self is AddTableWorkflowGroupRequestOutputColumnsItemType.SELECT:
            return select()
