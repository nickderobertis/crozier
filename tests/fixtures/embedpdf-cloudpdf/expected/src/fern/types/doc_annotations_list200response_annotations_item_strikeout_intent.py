

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemStrikeoutIntent(enum.StrEnum):
    STRIKEOUT_TEXT_EDIT = "strikeout-text-edit"

    def visit(self, strikeout_text_edit: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemStrikeoutIntent.STRIKEOUT_TEXT_EDIT:
            return strikeout_text_edit()
