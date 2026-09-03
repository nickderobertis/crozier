

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostTokenV2RequestGrantType(enum.StrEnum):
    """
    Authorization code grant type.
    """

    AUTHORIZATION_CODE = "authorization_code"

    def visit(self, authorization_code: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostTokenV2RequestGrantType.AUTHORIZATION_CODE:
            return authorization_code()
