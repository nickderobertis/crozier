

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountObject(enum.StrEnum):
    """
    Object type identifier
    """

    ACCOUNT = "account"

    def visit(self, account: typing.Callable[[], T_Result]) -> T_Result:
        if self is AccountObject.ACCOUNT:
            return account()
