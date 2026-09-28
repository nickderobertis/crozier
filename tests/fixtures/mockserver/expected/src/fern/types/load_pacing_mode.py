

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadPacingMode(enum.StrEnum):
    """
    how the target iteration cycle is derived from value: NONE = no pacing (immediate reschedule); CONSTANT_PACING = value is the target cycle in milliseconds; CONSTANT_THROUGHPUT = value is the target iterations/second per VU (cycle = 1000 / value ms)
    """

    NONE = "NONE"
    CONSTANT_PACING = "CONSTANT_PACING"
    CONSTANT_THROUGHPUT = "CONSTANT_THROUGHPUT"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        constant_pacing: typing.Callable[[], T_Result],
        constant_throughput: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadPacingMode.NONE:
            return none()
        if self is LoadPacingMode.CONSTANT_PACING:
            return constant_pacing()
        if self is LoadPacingMode.CONSTANT_THROUGHPUT:
            return constant_throughput()
