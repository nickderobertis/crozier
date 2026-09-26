

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RankingOptionBlockGroupType(enum.StrEnum):
    RANKING = "RANKING"

    def visit(self, ranking: typing.Callable[[], T_Result]) -> T_Result:
        if self is RankingOptionBlockGroupType.RANKING:
            return ranking()
