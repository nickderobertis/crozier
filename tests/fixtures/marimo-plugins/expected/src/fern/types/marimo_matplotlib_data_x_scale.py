

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoMatplotlibDataXScale(enum.StrEnum):
    LINEAR = "linear"
    LOG = "log"

    def visit(self, linear: typing.Callable[[], T_Result], log: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoMatplotlibDataXScale.LINEAR:
            return linear()
        if self is MarimoMatplotlibDataXScale.LOG:
            return log()
