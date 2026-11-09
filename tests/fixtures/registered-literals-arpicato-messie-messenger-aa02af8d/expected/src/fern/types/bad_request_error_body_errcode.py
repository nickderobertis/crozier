

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadRequestErrorBodyErrcode(enum.StrEnum):
    """
    A Matrix-like error code
    """

    M_NOT_JSON = "M_NOT_JSON"
    M_BAD_STATE = "M_BAD_STATE"

    def visit(self, m_not_json: typing.Callable[[], T_Result], m_bad_state: typing.Callable[[], T_Result]) -> T_Result:
        if self is BadRequestErrorBodyErrcode.M_NOT_JSON:
            return m_not_json()
        if self is BadRequestErrorBodyErrcode.M_BAD_STATE:
            return m_bad_state()
