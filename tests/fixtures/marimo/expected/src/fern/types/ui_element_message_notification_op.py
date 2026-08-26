

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UiElementMessageNotificationOp(enum.StrEnum):
    SEND_UI_ELEMENT_MESSAGE = "send-ui-element-message"

    def visit(self, send_ui_element_message: typing.Callable[[], T_Result]) -> T_Result:
        if self is UiElementMessageNotificationOp.SEND_UI_ELEMENT_MESSAGE:
            return send_ui_element_message()
