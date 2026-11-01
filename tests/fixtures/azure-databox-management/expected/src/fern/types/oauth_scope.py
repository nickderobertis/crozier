

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    USER_IMPERSONATION = "user_impersonation"
    """
    impersonate your user account
    """

    def visit(self, user_impersonation: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.USER_IMPERSONATION:
            return user_impersonation()
