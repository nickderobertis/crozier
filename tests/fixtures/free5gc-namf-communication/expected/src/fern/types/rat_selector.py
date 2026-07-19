

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RatSelector(enum.StrEnum):
    E_UTRA = "E-UTRA"
    NR = "NR"

    def visit(self, e_utra: typing.Callable[[], T_Result], nr: typing.Callable[[], T_Result]) -> T_Result:
        if self is RatSelector.E_UTRA:
            return e_utra()
        if self is RatSelector.NR:
            return nr()
