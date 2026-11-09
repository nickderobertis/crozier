

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenResponseDtoTokenType(enum.StrEnum):
    """
    The type of token issued (currently always 'Bearer')
    """

    BEARER = "Bearer"

    def visit(self, bearer: typing.Callable[[], T_Result]) -> T_Result:
        if self is TokenResponseDtoTokenType.BEARER:
            return bearer()
