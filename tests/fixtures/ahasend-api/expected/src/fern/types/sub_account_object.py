

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubAccountObject(enum.StrEnum):
    """
    Object type identifier
    """

    SUB_ACCOUNT = "sub_account"

    def visit(self, sub_account: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubAccountObject.SUB_ACCOUNT:
            return sub_account()
