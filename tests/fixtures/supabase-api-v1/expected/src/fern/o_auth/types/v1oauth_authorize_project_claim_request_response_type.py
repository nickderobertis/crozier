

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1OauthAuthorizeProjectClaimRequestResponseType(enum.StrEnum):
    CODE = "code"
    TOKEN = "token"
    ID_TOKEN_TOKEN = "id_token token"

    def visit(
        self,
        code: typing.Callable[[], T_Result],
        token: typing.Callable[[], T_Result],
        id_token_token: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1OauthAuthorizeProjectClaimRequestResponseType.CODE:
            return code()
        if self is V1OauthAuthorizeProjectClaimRequestResponseType.TOKEN:
            return token()
        if self is V1OauthAuthorizeProjectClaimRequestResponseType.ID_TOKEN_TOKEN:
            return id_token_token()
