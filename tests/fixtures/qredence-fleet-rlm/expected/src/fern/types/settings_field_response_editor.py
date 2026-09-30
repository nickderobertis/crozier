

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SettingsFieldResponseEditor(enum.StrEnum):
    TEXT = "text"
    NUMBER = "number"
    BOOLEAN = "boolean"
    SINGLE_CHOICE = "single_choice"
    MULTI_CHOICE = "multi_choice"
    STRING_LIST = "string_list"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
        single_choice: typing.Callable[[], T_Result],
        multi_choice: typing.Callable[[], T_Result],
        string_list: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SettingsFieldResponseEditor.TEXT:
            return text()
        if self is SettingsFieldResponseEditor.NUMBER:
            return number()
        if self is SettingsFieldResponseEditor.BOOLEAN:
            return boolean()
        if self is SettingsFieldResponseEditor.SINGLE_CHOICE:
            return single_choice()
        if self is SettingsFieldResponseEditor.MULTI_CHOICE:
            return multi_choice()
        if self is SettingsFieldResponseEditor.STRING_LIST:
            return string_list()
