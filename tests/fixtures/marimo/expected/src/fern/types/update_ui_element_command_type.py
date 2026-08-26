

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateUiElementCommandType(enum.StrEnum):
    UPDATE_UI_ELEMENT = "update-ui-element"

    def visit(self, update_ui_element: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateUiElementCommandType.UPDATE_UI_ELEMENT:
            return update_ui_element()
