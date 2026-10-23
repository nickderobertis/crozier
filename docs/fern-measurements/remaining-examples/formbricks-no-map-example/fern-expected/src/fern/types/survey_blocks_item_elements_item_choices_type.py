

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemChoicesType(enum.StrEnum):
    RANKING = "ranking"

    def visit(self, ranking: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemChoicesType.RANKING:
            return ranking()
