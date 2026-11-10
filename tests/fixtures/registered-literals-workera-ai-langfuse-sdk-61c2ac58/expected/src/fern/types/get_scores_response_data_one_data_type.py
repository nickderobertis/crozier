

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetScoresResponseDataOneDataType(enum.StrEnum):
    CATEGORICAL = "CATEGORICAL"

    def visit(self, categorical: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetScoresResponseDataOneDataType.CATEGORICAL:
            return categorical()
