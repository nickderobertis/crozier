

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    MANAGE = "manage"
    """
    Grants access
    """

    def visit(self, manage: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.MANAGE:
            return manage()
