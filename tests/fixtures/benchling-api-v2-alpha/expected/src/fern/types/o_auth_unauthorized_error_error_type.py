

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OAuthUnauthorizedErrorErrorType(enum.StrEnum):
    INVALID_CLIENT = "invalid_client"

    def visit(self, invalid_client: typing.Callable[[], T_Result]) -> T_Result:
        if self is OAuthUnauthorizedErrorErrorType.INVALID_CLIENT:
            return invalid_client()
