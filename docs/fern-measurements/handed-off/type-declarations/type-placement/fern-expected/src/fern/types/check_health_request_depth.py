

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CheckHealthRequestDepth(enum.StrEnum):
    SHALLOW = "shallow"
    DEEP = "deep"

    def visit(self, shallow: typing.Callable[[], T_Result], deep: typing.Callable[[], T_Result]) -> T_Result:
        if self is CheckHealthRequestDepth.SHALLOW:
            return shallow()
        if self is CheckHealthRequestDepth.DEEP:
            return deep()
