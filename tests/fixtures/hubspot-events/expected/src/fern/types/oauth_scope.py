

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    OAUTH = "oauth"
    """
    User and Account Information
    """

    def visit(self, oauth: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.OAUTH:
            return oauth()
