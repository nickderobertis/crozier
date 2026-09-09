

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProductsPatch422DetailsItemUserAccountClosedDescription(enum.StrEnum):
    USER_ACCOUNT_LOCKED_OR_CLOSED = "User account locked or closed."

    def visit(self, user_account_locked_or_closed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProductsPatch422DetailsItemUserAccountClosedDescription.USER_ACCOUNT_LOCKED_OR_CLOSED:
            return user_account_locked_or_closed()
