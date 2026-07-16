

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    ACCOUNTS = "accounts"
    """
    Ability to read Accounts information
    """

    def visit(self, accounts: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.ACCOUNTS:
            return accounts()
