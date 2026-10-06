

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListCoolingFiringsRequestAtmosphereOneItem(enum.StrEnum):
    OXIDATION = "oxidation"
    REDUCTION = "reduction"

    def visit(self, oxidation: typing.Callable[[], T_Result], reduction: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListCoolingFiringsRequestAtmosphereOneItem.OXIDATION:
            return oxidation()
        if self is ListCoolingFiringsRequestAtmosphereOneItem.REDUCTION:
            return reduction()
