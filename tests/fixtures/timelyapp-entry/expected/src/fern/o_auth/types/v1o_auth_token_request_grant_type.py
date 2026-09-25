

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1OAuthTokenRequestGrantType(enum.StrEnum):
    """
    OAuth 2.0 grant type
    """

    AUTHORIZATION_CODE = "authorization_code"
    REFRESH_TOKEN = "refresh_token"

    def visit(
        self, authorization_code: typing.Callable[[], T_Result], refresh_token: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is V1OAuthTokenRequestGrantType.AUTHORIZATION_CODE:
            return authorization_code()
        if self is V1OAuthTokenRequestGrantType.REFRESH_TOKEN:
            return refresh_token()
