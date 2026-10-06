

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SeriesSpecInterpolationOneNine(enum.StrEnum):
    """
    Interpolate with a polynomial of the lowest possible degree passing trough the data points.
    """

    POLYNOMIAL = "polynomial"

    def visit(self, polynomial: typing.Callable[[], T_Result]) -> T_Result:
        if self is SeriesSpecInterpolationOneNine.POLYNOMIAL:
            return polynomial()
