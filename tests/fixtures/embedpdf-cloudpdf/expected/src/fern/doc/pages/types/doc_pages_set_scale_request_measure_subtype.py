

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesSetScaleRequestMeasureSubtype(enum.StrEnum):
    RL = "RL"

    def visit(self, rl: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocPagesSetScaleRequestMeasureSubtype.RL:
            return rl()
