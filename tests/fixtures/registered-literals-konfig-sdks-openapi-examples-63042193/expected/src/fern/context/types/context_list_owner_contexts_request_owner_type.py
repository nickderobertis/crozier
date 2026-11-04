

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ContextListOwnerContextsRequestOwnerType(enum.StrEnum):
    ACCOUNT = "account"
    ORGANIZATION = "organization"

    def visit(self, account: typing.Callable[[], T_Result], organization: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContextListOwnerContextsRequestOwnerType.ACCOUNT:
            return account()
        if self is ContextListOwnerContextsRequestOwnerType.ORGANIZATION:
            return organization()
