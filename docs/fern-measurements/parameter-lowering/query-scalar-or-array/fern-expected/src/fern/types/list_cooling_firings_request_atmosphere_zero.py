

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListCoolingFiringsRequestAtmosphereZero(enum.StrEnum):
    OXIDATION = "oxidation"
    REDUCTION = "reduction"

    def visit(self, oxidation: typing.Callable[[], T_Result], reduction: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListCoolingFiringsRequestAtmosphereZero.OXIDATION:
            return oxidation()
        if self is ListCoolingFiringsRequestAtmosphereZero.REDUCTION:
            return reduction()
