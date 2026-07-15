

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ConnectorOauthGrantType(str, enum.Enum):
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
        if self is ConnectorOauthGrantType.AUTHORIZATION_CODE:
            return authorization_code()
        if self is ConnectorOauthGrantType.CLIENT_CREDENTIALS:
            return client_credentials()
        if self is ConnectorOauthGrantType.PASSWORD:
            return password()
