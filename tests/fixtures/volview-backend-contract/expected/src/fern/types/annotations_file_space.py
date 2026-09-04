

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AnnotationsFileSpace(enum.StrEnum):
    LPS = "LPS"

    def visit(self, lps: typing.Callable[[], T_Result]) -> T_Result:
        if self is AnnotationsFileSpace.LPS:
            return lps()
