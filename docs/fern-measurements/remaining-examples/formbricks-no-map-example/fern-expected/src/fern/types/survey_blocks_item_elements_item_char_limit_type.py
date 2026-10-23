

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemCharLimitType(enum.StrEnum):
    OPEN_TEXT = "openText"

    def visit(self, open_text: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemCharLimitType.OPEN_TEXT:
            return open_text()
