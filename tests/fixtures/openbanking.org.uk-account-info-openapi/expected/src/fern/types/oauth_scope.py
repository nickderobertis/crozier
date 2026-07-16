

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OauthScope(str, enum.Enum):
    ACCOUNTS = "accounts"
    """
    Ability to read Accounts information
    """

    def visit(self, accounts: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.ACCOUNTS:
            return accounts()
