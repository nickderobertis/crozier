

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryOutputInterpolationOneEleven(enum.StrEnum):
    """
    Interpolate with the derivative of order 1.
    """

    FROM_DERIVATIVES = "from_derivatives"

    def visit(self, from_derivatives: typing.Callable[[], T_Result]) -> T_Result:
        if self is QueryOutputInterpolationOneEleven.FROM_DERIVATIVES:
            return from_derivatives()
