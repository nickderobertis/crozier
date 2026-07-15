

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectorSettingType(str, enum.Enum):
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
    PASSWORD = "password"

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
        password: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConnectorSettingType.TEXT:
            return text()
        if self is ConnectorSettingType.CHECKBOX:
            return checkbox()
        if self is ConnectorSettingType.TEL:
            return tel()
        if self is ConnectorSettingType.EMAIL:
            return email()
        if self is ConnectorSettingType.URL:
            return url()
        if self is ConnectorSettingType.TEXTAREA:
            return textarea()
        if self is ConnectorSettingType.SELECT:
            return select()
        if self is ConnectorSettingType.FILTERED_SELECT:
            return filtered_select()
        if self is ConnectorSettingType.MULTI_SELECT:
            return multi_select()
        if self is ConnectorSettingType.DATETIME:
            return datetime()
        if self is ConnectorSettingType.DATE:
            return date()
        if self is ConnectorSettingType.TIME:
            return time()
        if self is ConnectorSettingType.NUMBER:
            return number()
        if self is ConnectorSettingType.PASSWORD:
            return password()
