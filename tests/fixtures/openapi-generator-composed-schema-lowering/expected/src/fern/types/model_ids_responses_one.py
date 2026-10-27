

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelIdsResponsesOne(enum.StrEnum):
    IDS = "ids"

    def visit(self, ids: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelIdsResponsesOne.IDS:
            return ids()
