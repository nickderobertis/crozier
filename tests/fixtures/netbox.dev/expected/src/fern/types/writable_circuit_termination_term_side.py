

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableCircuitTerminationTermSide(str, enum.Enum):
    A = "A"
    Z = "Z"

    def visit(self, a: typing.Callable[[], T_Result], z: typing.Callable[[], T_Result]) -> T_Result:
        if self is WritableCircuitTerminationTermSide.A:
            return a()
        if self is WritableCircuitTerminationTermSide.Z:
            return z()
