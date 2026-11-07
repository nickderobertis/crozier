

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OAuth2TokenResponseTokenType(enum.StrEnum):
    """
    Token type (always "Bearer" for this implementation)
    """

    BEARER = "Bearer"

    def visit(self, bearer: typing.Callable[[], T_Result]) -> T_Result:
        if self is OAuth2TokenResponseTokenType.BEARER:
            return bearer()
