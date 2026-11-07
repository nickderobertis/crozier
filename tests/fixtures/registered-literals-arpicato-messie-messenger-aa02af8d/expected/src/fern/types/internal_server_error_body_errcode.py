

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InternalServerErrorBodyErrcode(enum.StrEnum):
    """
    A Matrix-like error code
    """

    M_UNKNOWN = "M_UNKNOWN"

    def visit(self, m_unknown: typing.Callable[[], T_Result]) -> T_Result:
        if self is InternalServerErrorBodyErrcode.M_UNKNOWN:
            return m_unknown()
