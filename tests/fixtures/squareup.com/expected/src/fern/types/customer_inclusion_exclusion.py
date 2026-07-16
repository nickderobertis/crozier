

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerInclusionExclusion(enum.StrEnum):
    """
    Indicates whether customers should be included in, or excluded from,
    the result set when they match the filtering criteria.
    """

    INCLUDE = "INCLUDE"
    EXCLUDE = "EXCLUDE"

    def visit(self, include: typing.Callable[[], T_Result], exclude: typing.Callable[[], T_Result]) -> T_Result:
        if self is CustomerInclusionExclusion.INCLUDE:
            return include()
        if self is CustomerInclusionExclusion.EXCLUDE:
            return exclude()
