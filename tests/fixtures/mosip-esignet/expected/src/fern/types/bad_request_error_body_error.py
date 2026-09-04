

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadRequestErrorBodyError(enum.StrEnum):
    """
    Error code, available in error response.
    """

    INVALID_REQUEST = "invalid_request"
    INVALID_CLIENT_ID = "invalid_client_id"
    INVALID_REDIRECT_URI = "invalid_redirect_uri"
    INVALID_SCOPE = "invalid_scope"
    INVALID_ACR = "invalid_acr"
    INVALID_RESPONSE_TYPE = "invalid_response_type"
    INVALID_DISPLAY = "invalid_display"
    INVALID_PROMPT = "invalid_prompt"

    def visit(
        self,
        invalid_request: typing.Callable[[], T_Result],
        invalid_client_id: typing.Callable[[], T_Result],
        invalid_redirect_uri: typing.Callable[[], T_Result],
        invalid_scope: typing.Callable[[], T_Result],
        invalid_acr: typing.Callable[[], T_Result],
        invalid_response_type: typing.Callable[[], T_Result],
        invalid_display: typing.Callable[[], T_Result],
        invalid_prompt: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BadRequestErrorBodyError.INVALID_REQUEST:
            return invalid_request()
        if self is BadRequestErrorBodyError.INVALID_CLIENT_ID:
            return invalid_client_id()
        if self is BadRequestErrorBodyError.INVALID_REDIRECT_URI:
            return invalid_redirect_uri()
        if self is BadRequestErrorBodyError.INVALID_SCOPE:
            return invalid_scope()
        if self is BadRequestErrorBodyError.INVALID_ACR:
            return invalid_acr()
        if self is BadRequestErrorBodyError.INVALID_RESPONSE_TYPE:
            return invalid_response_type()
        if self is BadRequestErrorBodyError.INVALID_DISPLAY:
            return invalid_display()
        if self is BadRequestErrorBodyError.INVALID_PROMPT:
            return invalid_prompt()
