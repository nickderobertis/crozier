

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PredictionsSortBy(enum.StrEnum):
    CREATED_TIME = "createdTime"

    def visit(self, created_time: typing.Callable[[], T_Result]) -> T_Result:
        if self is PredictionsSortBy.CREATED_TIME:
            return created_time()
