

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryObjectType(enum.StrEnum):
    CANDIDATES = "candidates"

    def visit(self, candidates: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryObjectType.CANDIDATES:
            return candidates()
