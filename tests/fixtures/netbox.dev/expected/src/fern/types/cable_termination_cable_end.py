

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CableTerminationCableEnd(str, enum.Enum):
    A = "A"
    B = "B"

    def visit(self, a: typing.Callable[[], T_Result], b: typing.Callable[[], T_Result]) -> T_Result:
        if self is CableTerminationCableEnd.A:
            return a()
        if self is CableTerminationCableEnd.B:
            return b()
