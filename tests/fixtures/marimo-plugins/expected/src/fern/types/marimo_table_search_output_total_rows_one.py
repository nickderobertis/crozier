

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoTableSearchOutputTotalRowsOne(enum.StrEnum):
    TOO_MANY = "too_many"

    def visit(self, too_many: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoTableSearchOutputTotalRowsOne.TOO_MANY:
            return too_many()
