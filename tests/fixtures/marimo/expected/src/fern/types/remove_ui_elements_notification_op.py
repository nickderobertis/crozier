

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoveUiElementsNotificationOp(enum.StrEnum):
    REMOVE_UI_ELEMENTS = "remove-ui-elements"

    def visit(self, remove_ui_elements: typing.Callable[[], T_Result]) -> T_Result:
        if self is RemoveUiElementsNotificationOp.REMOVE_UI_ELEMENTS:
            return remove_ui_elements()
