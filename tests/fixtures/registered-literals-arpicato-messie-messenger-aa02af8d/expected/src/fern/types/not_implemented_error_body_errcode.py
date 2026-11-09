

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotImplementedErrorBodyErrcode(enum.StrEnum):
    """
    A Matrix-like error code
    """

    M_UNRECOGNIZED = "M_UNRECOGNIZED"

    def visit(self, m_unrecognized: typing.Callable[[], T_Result]) -> T_Result:
        if self is NotImplementedErrorBodyErrcode.M_UNRECOGNIZED:
            return m_unrecognized()
