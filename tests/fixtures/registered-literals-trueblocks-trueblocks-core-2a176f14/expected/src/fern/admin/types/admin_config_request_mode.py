

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AdminConfigRequestMode(enum.StrEnum):
    SHOW = "show"
    EDIT = "edit"

    def visit(self, show: typing.Callable[[], T_Result], edit: typing.Callable[[], T_Result]) -> T_Result:
        if self is AdminConfigRequestMode.SHOW:
            return show()
        if self is AdminConfigRequestMode.EDIT:
            return edit()
