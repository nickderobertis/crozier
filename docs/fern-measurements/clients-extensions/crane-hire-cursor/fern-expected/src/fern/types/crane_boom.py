

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CraneBoom(enum.StrEnum):
    LATTICE = "lattice"
    TELESCOPIC = "telescopic"

    def visit(self, lattice: typing.Callable[[], T_Result], telescopic: typing.Callable[[], T_Result]) -> T_Result:
        if self is CraneBoom.LATTICE:
            return lattice()
        if self is CraneBoom.TELESCOPIC:
            return telescopic()
