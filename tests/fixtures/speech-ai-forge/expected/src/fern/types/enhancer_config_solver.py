

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnhancerConfigSolver(enum.StrEnum):
    MIDPOINT = "midpoint"
    RK4 = "rk4"
    EULER = "euler"

    def visit(
        self,
        midpoint: typing.Callable[[], T_Result],
        rk4: typing.Callable[[], T_Result],
        euler: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnhancerConfigSolver.MIDPOINT:
            return midpoint()
        if self is EnhancerConfigSolver.RK4:
            return rk4()
        if self is EnhancerConfigSolver.EULER:
            return euler()
