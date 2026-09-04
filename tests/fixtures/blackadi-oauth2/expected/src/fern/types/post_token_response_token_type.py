

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostTokenResponseTokenType(enum.StrEnum):
    BEARER = "Bearer"

    def visit(self, bearer: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostTokenResponseTokenType.BEARER:
            return bearer()
