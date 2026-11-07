

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotFoundErrorBodyErrcode(enum.StrEnum):
    """
    A Matrix-like error code
    """

    M_NOT_FOUND = "M_NOT_FOUND"

    def visit(self, m_not_found: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotFoundErrorBodyErrcode.M_NOT_FOUND:
            return m_not_found()
