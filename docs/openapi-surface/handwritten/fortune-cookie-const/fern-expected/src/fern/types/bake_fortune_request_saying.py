

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BakeFortuneRequestSaying(enum.StrEnum):
    YOULL_FIND_IT = "You'll find it"

    def visit(self, youll_find_it: typing.Callable[[], T_Result]) -> T_Result:
        if self is BakeFortuneRequestSaying.YOULL_FIND_IT:
            return youll_find_it()
