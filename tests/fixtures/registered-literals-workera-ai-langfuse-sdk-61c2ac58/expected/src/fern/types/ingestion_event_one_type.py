

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IngestionEventOneType(enum.StrEnum):
    SCORE_CREATE = "score-create"

    def visit(self, score_create: typing.Callable[[], T_Result]) -> T_Result:
        if self is IngestionEventOneType.SCORE_CREATE:
            return score_create()
