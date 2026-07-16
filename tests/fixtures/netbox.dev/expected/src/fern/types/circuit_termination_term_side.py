

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CircuitTerminationTermSide(enum.StrEnum):
    A = "A"
    Z = "Z"

    def visit(self, a: typing.Callable[[], T_Result], z: typing.Callable[[], T_Result]) -> T_Result:
        if self is CircuitTerminationTermSide.A:
            return a()
        if self is CircuitTerminationTermSide.Z:
            return z()
