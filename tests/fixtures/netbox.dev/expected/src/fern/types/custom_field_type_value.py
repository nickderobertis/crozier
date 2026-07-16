

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CustomFieldTypeValue(str, enum.Enum):
    TEXT = "text"
    LONGTEXT = "longtext"
    INTEGER = "integer"
    DECIMAL = "decimal"
    BOOLEAN = "boolean"
    DATE = "date"
    URL = "url"
    JSON = "json"
    SELECT = "select"
    MULTISELECT = "multiselect"
    OBJECT = "object"
    MULTIOBJECT = "multiobject"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        longtext: typing.Callable[[], T_Result],
        integer: typing.Callable[[], T_Result],
        decimal: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        json: typing.Callable[[], T_Result],
        select: typing.Callable[[], T_Result],
        multiselect: typing.Callable[[], T_Result],
        object: typing.Callable[[], T_Result],
        multiobject: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomFieldTypeValue.TEXT:
            return text()
        if self is CustomFieldTypeValue.LONGTEXT:
            return longtext()
        if self is CustomFieldTypeValue.INTEGER:
            return integer()
        if self is CustomFieldTypeValue.DECIMAL:
            return decimal()
        if self is CustomFieldTypeValue.BOOLEAN:
            return boolean()
        if self is CustomFieldTypeValue.DATE:
            return date()
        if self is CustomFieldTypeValue.URL:
            return url()
        if self is CustomFieldTypeValue.JSON:
            return json()
        if self is CustomFieldTypeValue.SELECT:
            return select()
        if self is CustomFieldTypeValue.MULTISELECT:
            return multiselect()
        if self is CustomFieldTypeValue.OBJECT:
            return object()
        if self is CustomFieldTypeValue.MULTIOBJECT:
            return multiobject()
