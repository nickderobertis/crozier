

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateTableWorkflowGroupRequestNewOutputColumnsItemType(enum.StrEnum):
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
        if self is UpdateTableWorkflowGroupRequestNewOutputColumnsItemType.STRING:
            return string()
        if self is UpdateTableWorkflowGroupRequestNewOutputColumnsItemType.NUMBER:
            return number()
        if self is UpdateTableWorkflowGroupRequestNewOutputColumnsItemType.CURRENCY:
            return currency()
        if self is UpdateTableWorkflowGroupRequestNewOutputColumnsItemType.BOOLEAN:
            return boolean()
        if self is UpdateTableWorkflowGroupRequestNewOutputColumnsItemType.DATE:
            return date()
        if self is UpdateTableWorkflowGroupRequestNewOutputColumnsItemType.JSON:
            return json()
        if self is UpdateTableWorkflowGroupRequestNewOutputColumnsItemType.SELECT:
            return select()
