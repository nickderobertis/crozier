

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomiseType(enum.StrEnum):
    """
    field type
    """

    INT = "int"
    TEXT = "text"
    TEXTAREA = "textarea"
    PASSWORD = "password"
    DROPDOWN = "dropdown"
    BOOLEAN = "boolean"

    def visit(
        self,
        int_: typing.Callable[[], T_Result],
        text: typing.Callable[[], T_Result],
        textarea: typing.Callable[[], T_Result],
        password: typing.Callable[[], T_Result],
        dropdown: typing.Callable[[], T_Result],
        boolean: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomiseType.INT:
            return int_()
        if self is CustomiseType.TEXT:
            return text()
        if self is CustomiseType.TEXTAREA:
            return textarea()
        if self is CustomiseType.PASSWORD:
            return password()
        if self is CustomiseType.DROPDOWN:
            return dropdown()
        if self is CustomiseType.BOOLEAN:
            return boolean()
