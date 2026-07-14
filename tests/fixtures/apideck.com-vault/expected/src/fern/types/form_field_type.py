

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FormFieldType(str, enum.Enum):
    TEXT = "text"
    CHECKBOX = "checkbox"
    TEL = "tel"
    EMAIL = "email"
    URL = "url"
    TEXTAREA = "textarea"
    SELECT = "select"
    FILTERED_SELECT = "filtered-select"
    MULTI_SELECT = "multi-select"
    DATETIME = "datetime"
    DATE = "date"
    TIME = "time"
    NUMBER = "number"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        checkbox: typing.Callable[[], T_Result],
        tel: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
        textarea: typing.Callable[[], T_Result],
        select: typing.Callable[[], T_Result],
        filtered_select: typing.Callable[[], T_Result],
        multi_select: typing.Callable[[], T_Result],
        datetime: typing.Callable[[], T_Result],
        date: typing.Callable[[], T_Result],
        time: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FormFieldType.TEXT:
            return text()
        if self is FormFieldType.CHECKBOX:
            return checkbox()
        if self is FormFieldType.TEL:
            return tel()
        if self is FormFieldType.EMAIL:
            return email()
        if self is FormFieldType.URL:
            return url()
        if self is FormFieldType.TEXTAREA:
            return textarea()
        if self is FormFieldType.SELECT:
            return select()
        if self is FormFieldType.FILTERED_SELECT:
            return filtered_select()
        if self is FormFieldType.MULTI_SELECT:
            return multi_select()
        if self is FormFieldType.DATETIME:
            return datetime()
        if self is FormFieldType.DATE:
            return date()
        if self is FormFieldType.TIME:
            return time()
        if self is FormFieldType.NUMBER:
            return number()
