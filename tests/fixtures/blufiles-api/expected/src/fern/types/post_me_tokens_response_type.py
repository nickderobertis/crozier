

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostMeTokensResponseType(enum.StrEnum):
    USER = "user"
    UPLOADER = "uploader"

    def visit(self, user: typing.Callable[[], T_Result], uploader: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostMeTokensResponseType.USER:
            return user()
        if self is PostMeTokensResponseType.UPLOADER:
            return uploader()
