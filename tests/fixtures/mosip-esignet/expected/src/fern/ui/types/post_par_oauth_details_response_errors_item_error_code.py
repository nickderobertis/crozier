

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostParOauthDetailsResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_CLIENT_ID = "invalid_client_id"
    INVALID_REDIRECT_URI = "invalid_redirect_uri"
    INVALID_SCOPE = "invalid_scope"
    NO_ACR_REGISTERED = "no_acr_registered"
    INVALID_RESPONSE_TYPE = "invalid_response_type"
    INVALID_DISPLAY = "invalid_display"
    INVALID_PROMPT = "invalid_prompt"
    UNSUPPORTED_PKCE_CHALLENGE_METHOD = "unsupported_pkce_challenge_method"
    INVALID_PKCE_CHALLENGE = "invalid_pkce_challenge"
    INVALID_REQUEST = "invalid_request"
    INVALID_ID_TOKEN_HINT = "invalid_id_token_hint"

    def visit(
        self,
        invalid_client_id: typing.Callable[[], T_Result],
        invalid_redirect_uri: typing.Callable[[], T_Result],
        invalid_scope: typing.Callable[[], T_Result],
        no_acr_registered: typing.Callable[[], T_Result],
        invalid_response_type: typing.Callable[[], T_Result],
        invalid_display: typing.Callable[[], T_Result],
        invalid_prompt: typing.Callable[[], T_Result],
        unsupported_pkce_challenge_method: typing.Callable[[], T_Result],
        invalid_pkce_challenge: typing.Callable[[], T_Result],
        invalid_request: typing.Callable[[], T_Result],
        invalid_id_token_hint: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostParOauthDetailsResponseErrorsItemErrorCode.INVALID_CLIENT_ID:
            return invalid_client_id()
        if self is PostParOauthDetailsResponseErrorsItemErrorCode.INVALID_REDIRECT_URI:
            return invalid_redirect_uri()
        if self is PostParOauthDetailsResponseErrorsItemErrorCode.INVALID_SCOPE:
            return invalid_scope()
        if self is PostParOauthDetailsResponseErrorsItemErrorCode.NO_ACR_REGISTERED:
            return no_acr_registered()
        if self is PostParOauthDetailsResponseErrorsItemErrorCode.INVALID_RESPONSE_TYPE:
            return invalid_response_type()
        if self is PostParOauthDetailsResponseErrorsItemErrorCode.INVALID_DISPLAY:
            return invalid_display()
        if self is PostParOauthDetailsResponseErrorsItemErrorCode.INVALID_PROMPT:
            return invalid_prompt()
        if self is PostParOauthDetailsResponseErrorsItemErrorCode.UNSUPPORTED_PKCE_CHALLENGE_METHOD:
            return unsupported_pkce_challenge_method()
        if self is PostParOauthDetailsResponseErrorsItemErrorCode.INVALID_PKCE_CHALLENGE:
            return invalid_pkce_challenge()
        if self is PostParOauthDetailsResponseErrorsItemErrorCode.INVALID_REQUEST:
            return invalid_request()
        if self is PostParOauthDetailsResponseErrorsItemErrorCode.INVALID_ID_TOKEN_HINT:
            return invalid_id_token_hint()
