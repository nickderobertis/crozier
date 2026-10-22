

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemAllowMultiType(enum.StrEnum):
    PICTURE_SELECTION = "pictureSelection"

    def visit(self, picture_selection: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemAllowMultiType.PICTURE_SELECTION:
            return picture_selection()
