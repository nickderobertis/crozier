

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoMatplotlibDataYScale(enum.StrEnum):
    LINEAR = "linear"
    LOG = "log"

    def visit(self, linear: typing.Callable[[], T_Result], log: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoMatplotlibDataYScale.LINEAR:
            return linear()
        if self is MarimoMatplotlibDataYScale.LOG:
            return log()
