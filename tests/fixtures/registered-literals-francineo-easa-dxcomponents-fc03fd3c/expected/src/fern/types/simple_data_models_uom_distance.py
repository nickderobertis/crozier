

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SimpleDataModelsUomDistance(enum.StrEnum):
    """
    The unit of measurement in which the upper and lower values are expressed.
    If this member is not specified, the units should be assumed to be metres.
    """

    M = "m"
    FT = "ft"

    def visit(self, m: typing.Callable[[], T_Result], ft: typing.Callable[[], T_Result]) -> T_Result:
        if self is SimpleDataModelsUomDistance.M:
            return m()
        if self is SimpleDataModelsUomDistance.FT:
            return ft()
