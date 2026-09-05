

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WidgetType(enum.StrEnum):
    TEXT_AREA = "TextArea"
    SELECT_BOX = "SelectBox"

    def visit(self, text_area: typing.Callable[[], T_Result], select_box: typing.Callable[[], T_Result]) -> T_Result:
        if self is WidgetType.TEXT_AREA:
            return text_area()
        if self is WidgetType.SELECT_BOX:
            return select_box()
