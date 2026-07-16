

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomFieldTypeLabel(enum.StrEnum):
    TEXT = "Text"
    TEXT_LONG = "Text (long)"
    INTEGER = "Integer"
    DECIMAL = "Decimal"
    BOOLEAN_TRUE_FALSE = "Boolean (true/false)"
    DATE = "Date"
    URL = "URL"
    JSON = "JSON"
    SELECTION = "Selection"
    MULTIPLE_SELECTION = "Multiple selection"
    OBJECT = "Object"
    MULTIPLE_OBJECTS = "Multiple objects"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        text_long: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        decimal: typing.Callable[[], T_Result],
        boolean_true_false: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        selection: typing.Callable[[], T_Result],
        multiple_selection: typing.Callable[[], T_Result],
        object: typing.Callable[[], T_Result],
        multiple_objects: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomFieldTypeLabel.TEXT:
            return text()
        if self is CustomFieldTypeLabel.TEXT_LONG:
            return text_long()
        if self is CustomFieldTypeLabel.INTEGER:
            return integer()
        if self is CustomFieldTypeLabel.DECIMAL:
            return decimal()
        if self is CustomFieldTypeLabel.BOOLEAN_TRUE_FALSE:
            return boolean_true_false()
        if self is CustomFieldTypeLabel.DATE:
            return date()
        if self is CustomFieldTypeLabel.URL:
            return url()
        if self is CustomFieldTypeLabel.JSON:
            return json()
        if self is CustomFieldTypeLabel.SELECTION:
            return selection()
        if self is CustomFieldTypeLabel.MULTIPLE_SELECTION:
            return multiple_selection()
        if self is CustomFieldTypeLabel.OBJECT:
            return object()
        if self is CustomFieldTypeLabel.MULTIPLE_OBJECTS:
            return multiple_objects()
