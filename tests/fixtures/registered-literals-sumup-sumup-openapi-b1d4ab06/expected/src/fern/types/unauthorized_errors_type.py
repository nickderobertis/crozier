

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UnauthorizedErrorsType(enum.StrEnum):
    """
    Key indicating type of error. Present only for typed 401 responses (e.g. invalid token, invalid password). Absent for generic unauthorized responses.
    """

    INVALID_ACCESS_TOKEN = "INVALID_ACCESS_TOKEN"
    INVALID_PASSWORD = "INVALID_PASSWORD"

    def visit(
        self, invalid_access_token: typing.Callable[[], T_Result], invalid_password: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is UnauthorizedErrorsType.INVALID_ACCESS_TOKEN:
            return invalid_access_token()
        if self is UnauthorizedErrorsType.INVALID_PASSWORD:
            return invalid_password()
