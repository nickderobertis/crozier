

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DedupTestOne(enum.StrEnum):
    A = "a"
    B = "b"

    def visit(self, a: typing.Callable[[], T_Result], b: typing.Callable[[], T_Result]) -> T_Result:
        if self is DedupTestOne.A:
            return a()
        if self is DedupTestOne.B:
            return b()
