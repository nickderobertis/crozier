

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TokenExchangeRequestGrantType(enum.StrEnum):
    """
    The OAuth2 grant type:
    - `urn:ietf:params:oauth:grant-type:token-exchange` for RFC 8693 token exchange
    - `authorization_code` for standard OAuth2 authorization code flow (proxied or local/hybrid)
    - `client_credentials` for broker-issued client credentials (local/hybrid mode)
    """

    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE = "urn:ietf:params:oauth:grant-type:token-exchange"
    AUTHORIZATION_CODE = "authorization_code"
    CLIENT_CREDENTIALS = "client_credentials"

    def visit(
        self,
        urn_ietf_params_oauth_grant_type_token_exchange: typing.Callable[[], T_Result],
        authorization_code: typing.Callable[[], T_Result],
        client_credentials: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TokenExchangeRequestGrantType.URN_IETF_PARAMS_OAUTH_GRANT_TYPE_TOKEN_EXCHANGE:
            return urn_ietf_params_oauth_grant_type_token_exchange()
        if self is TokenExchangeRequestGrantType.AUTHORIZATION_CODE:
            return authorization_code()
        if self is TokenExchangeRequestGrantType.CLIENT_CREDENTIALS:
            return client_credentials()
