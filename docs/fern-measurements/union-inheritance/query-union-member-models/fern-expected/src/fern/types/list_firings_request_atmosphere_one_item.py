

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListFiringsRequestAtmosphereOneItem(enum.StrEnum):
    OXIDATION = "oxidation"
    REDUCTION = "reduction"
    NEUTRAL = "neutral"

    def visit(
        self,
        oxidation: typing.Callable[[], T_Result],
        reduction: typing.Callable[[], T_Result],
        neutral: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListFiringsRequestAtmosphereOneItem.OXIDATION:
            return oxidation()
        if self is ListFiringsRequestAtmosphereOneItem.REDUCTION:
            return reduction()
        if self is ListFiringsRequestAtmosphereOneItem.NEUTRAL:
            return neutral()
