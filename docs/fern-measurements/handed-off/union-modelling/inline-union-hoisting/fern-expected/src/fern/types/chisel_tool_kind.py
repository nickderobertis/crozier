

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChiselToolKind(enum.StrEnum):
    CHISEL = "chisel"

    def visit(self, chisel: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChiselToolKind.CHISEL:
            return chisel()
