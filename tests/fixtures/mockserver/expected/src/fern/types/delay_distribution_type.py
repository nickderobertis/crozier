

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DelayDistributionType(enum.StrEnum):
    UNIFORM = "UNIFORM"
    LOG_NORMAL = "LOG_NORMAL"
    GAUSSIAN = "GAUSSIAN"

    def visit(
        self,
        uniform: typing.Callable[[], T_Result],
        log_normal: typing.Callable[[], T_Result],
        gaussian: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DelayDistributionType.UNIFORM:
            return uniform()
        if self is DelayDistributionType.LOG_NORMAL:
            return log_normal()
        if self is DelayDistributionType.GAUSSIAN:
            return gaussian()
