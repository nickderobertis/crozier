

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListFiringsRequestAtmosphereZero(enum.StrEnum):
    OXIDATION = "oxidation"
    REDUCTION = "reduction"
    NEUTRAL = "neutral"

    def visit(
        self,
        oxidation: typing.Callable[[], T_Result],
        reduction: typing.Callable[[], T_Result],
        neutral: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListFiringsRequestAtmosphereZero.OXIDATION:
            return oxidation()
        if self is ListFiringsRequestAtmosphereZero.REDUCTION:
            return reduction()
        if self is ListFiringsRequestAtmosphereZero.NEUTRAL:
            return neutral()
