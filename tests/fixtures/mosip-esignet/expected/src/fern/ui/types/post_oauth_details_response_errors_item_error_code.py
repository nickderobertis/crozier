

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostOauthDetailsResponseErrorsItemErrorCode(enum.StrEnum):
    INVALID_CLIENT_ID = "invalid_client_id"
    INVALID_REDIRECT_URI = "invalid_redirect_uri"
    INVALID_SCOPE = "invalid_scope"
    INVALID_RESPONSE_TYPE = "invalid_response_type"
    INVALID_DISPLAY = "invalid_display"
    INVALID_PROMPT = "invalid_prompt"

    def visit(
        self,
        invalid_client_id: typing.Callable[[], T_Result],
        invalid_redirect_uri: typing.Callable[[], T_Result],
        invalid_scope: typing.Callable[[], T_Result],
        invalid_response_type: typing.Callable[[], T_Result],
        invalid_display: typing.Callable[[], T_Result],
        invalid_prompt: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostOauthDetailsResponseErrorsItemErrorCode.INVALID_CLIENT_ID:
            return invalid_client_id()
        if self is PostOauthDetailsResponseErrorsItemErrorCode.INVALID_REDIRECT_URI:
            return invalid_redirect_uri()
        if self is PostOauthDetailsResponseErrorsItemErrorCode.INVALID_SCOPE:
            return invalid_scope()
        if self is PostOauthDetailsResponseErrorsItemErrorCode.INVALID_RESPONSE_TYPE:
            return invalid_response_type()
        if self is PostOauthDetailsResponseErrorsItemErrorCode.INVALID_DISPLAY:
            return invalid_display()
        if self is PostOauthDetailsResponseErrorsItemErrorCode.INVALID_PROMPT:
            return invalid_prompt()
