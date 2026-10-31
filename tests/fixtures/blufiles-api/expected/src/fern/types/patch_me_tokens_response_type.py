

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PatchMeTokensResponseType(enum.StrEnum):
    USER = "user"
    UPLOADER = "uploader"

    def visit(self, user: typing.Callable[[], T_Result], uploader: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchMeTokensResponseType.USER:
            return user()
        if self is PatchMeTokensResponseType.UPLOADER:
            return uploader()
