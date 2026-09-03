

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostOauthParRequestResponseType(enum.StrEnum):
    """
    Value that determines the authorization processing flow to be used. When using the Authorization Code Flow, this value is code.
    """

    CODE = "code"

    def visit(self, code: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostOauthParRequestResponseType.CODE:
            return code()
