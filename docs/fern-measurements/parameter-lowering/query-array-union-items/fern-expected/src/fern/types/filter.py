

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Filter(enum.StrEnum):
    LUMINANCE = "luminance"
    HYDROGEN_ALPHA = "hydrogen-alpha"
    OXYGEN_III = "oxygen-iii"

    def visit(
        self,
        luminance: typing.Callable[[], T_Result],
        hydrogen_alpha: typing.Callable[[], T_Result],
        oxygen_iii: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Filter.LUMINANCE:
            return luminance()
        if self is Filter.HYDROGEN_ALPHA:
            return hydrogen_alpha()
        if self is Filter.OXYGEN_III:
            return oxygen_iii()
