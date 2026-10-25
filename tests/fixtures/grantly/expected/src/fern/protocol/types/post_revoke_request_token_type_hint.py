

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostRevokeRequestTokenTypeHint(enum.StrEnum):
    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"

    def visit(
        self, access_token: typing.Callable[[], T_Result], refresh_token: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PostRevokeRequestTokenTypeHint.ACCESS_TOKEN:
            return access_token()
        if self is PostRevokeRequestTokenTypeHint.REFRESH_TOKEN:
            return refresh_token()
