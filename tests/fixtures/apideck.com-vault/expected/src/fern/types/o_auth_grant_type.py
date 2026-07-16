

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OAuthGrantType(enum.StrEnum):
    """
    OAuth grant type used by the connector. More info: https://oauth.net/2/grant-types
    """

    AUTHORIZATION_CODE = "authorization_code"
    CLIENT_CREDENTIALS = "client_credentials"
    PASSWORD = "password"

    def visit(
        self,
        authorization_code: typing.Callable[[], T_Result],
        client_credentials: typing.Callable[[], T_Result],
        password: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OAuthGrantType.AUTHORIZATION_CODE:
            return authorization_code()
        if self is OAuthGrantType.CLIENT_CREDENTIALS:
            return client_credentials()
        if self is OAuthGrantType.PASSWORD:
            return password()
