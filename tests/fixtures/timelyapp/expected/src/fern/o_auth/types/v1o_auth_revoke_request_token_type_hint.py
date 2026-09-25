

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1OAuthRevokeRequestTokenTypeHint(enum.StrEnum):
    """
    Hint about the type of token being revoked
    """

    ACCESS_TOKEN = "access_token"
    REFRESH_TOKEN = "refresh_token"

    def visit(
        self, access_token: typing.Callable[[], T_Result], refresh_token: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is V1OAuthRevokeRequestTokenTypeHint.ACCESS_TOKEN:
            return access_token()
        if self is V1OAuthRevokeRequestTokenTypeHint.REFRESH_TOKEN:
            return refresh_token()
