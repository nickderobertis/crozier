

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableCustomFieldType(str, enum.Enum):
    """
    The type of data this custom field holds
    """

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
        if self is WritableCustomFieldType.TEXT:
            return text()
        if self is WritableCustomFieldType.LONGTEXT:
            return longtext()
        if self is WritableCustomFieldType.INTEGER:
            return integer()
        if self is WritableCustomFieldType.DECIMAL:
            return decimal()
        if self is WritableCustomFieldType.BOOLEAN:
            return boolean()
        if self is WritableCustomFieldType.DATE:
            return date()
        if self is WritableCustomFieldType.URL:
            return url()
        if self is WritableCustomFieldType.JSON:
            return json()
        if self is WritableCustomFieldType.SELECT:
            return select()
        if self is WritableCustomFieldType.MULTISELECT:
            return multiselect()
        if self is WritableCustomFieldType.OBJECT:
            return object()
        if self is WritableCustomFieldType.MULTIOBJECT:
            return multiobject()
