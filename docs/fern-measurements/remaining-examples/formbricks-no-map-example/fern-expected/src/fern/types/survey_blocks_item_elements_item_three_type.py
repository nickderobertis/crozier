

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemThreeType(enum.StrEnum):
    NPS = "nps"

    def visit(self, nps: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemThreeType.NPS:
            return nps()
