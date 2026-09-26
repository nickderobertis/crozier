

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutIntent(enum.StrEnum):
    STRIKEOUT_TEXT_EDIT = "strikeout-text-edit"

    def visit(self, strikeout_text_edit: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemStrikeoutIntent.STRIKEOUT_TEXT_EDIT:
            return strikeout_text_edit()
