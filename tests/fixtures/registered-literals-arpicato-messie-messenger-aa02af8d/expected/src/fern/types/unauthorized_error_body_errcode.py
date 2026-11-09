

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UnauthorizedErrorBodyErrcode(enum.StrEnum):
    """
    A Matrix-like error code
    """

    M_UNKNOWN_TOKEN = "M_UNKNOWN_TOKEN"
    M_MISSING_TOKEN = "M_MISSING_TOKEN"

    def visit(
        self, m_unknown_token: typing.Callable[[], T_Result], m_missing_token: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is UnauthorizedErrorBodyErrcode.M_UNKNOWN_TOKEN:
            return m_unknown_token()
        if self is UnauthorizedErrorBodyErrcode.M_MISSING_TOKEN:
            return m_missing_token()
