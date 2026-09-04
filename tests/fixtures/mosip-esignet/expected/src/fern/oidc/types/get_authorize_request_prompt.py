

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAuthorizeRequestPrompt(enum.StrEnum):
    NONE = "none"
    LOGIN = "login"
    CONSENT = "consent"
    SELECT_ACCOUNT = "select_account"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        login: typing.Callable[[], T_Result],
        consent: typing.Callable[[], T_Result],
        select_account: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAuthorizeRequestPrompt.NONE:
            return none()
        if self is GetAuthorizeRequestPrompt.LOGIN:
            return login()
        if self is GetAuthorizeRequestPrompt.CONSENT:
            return consent()
        if self is GetAuthorizeRequestPrompt.SELECT_ACCOUNT:
            return select_account()
