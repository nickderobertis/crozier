

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetAuthorizationRequestPrompt(enum.StrEnum):
    NONE = "none"
    LOGIN = "login"
    CONSENT = "consent"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        login: typing.Callable[[], T_Result],
        consent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAuthorizationRequestPrompt.NONE:
            return none()
        if self is GetAuthorizationRequestPrompt.LOGIN:
            return login()
        if self is GetAuthorizationRequestPrompt.CONSENT:
            return consent()
