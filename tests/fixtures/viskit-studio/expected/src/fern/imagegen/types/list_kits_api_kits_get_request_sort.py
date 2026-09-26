

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListKitsApiKitsGetRequestSort(enum.StrEnum):
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    SCORE = "score"

    def visit(
        self,
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
        score: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListKitsApiKitsGetRequestSort.CREATED_AT:
            return created_at()
        if self is ListKitsApiKitsGetRequestSort.UPDATED_AT:
            return updated_at()
        if self is ListKitsApiKitsGetRequestSort.SCORE:
            return score()
