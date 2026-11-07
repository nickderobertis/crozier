

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ContextCreateNewContextRequestOwnerIdType(enum.StrEnum):
    """
    The type of the owner. Defaults to "organization". Accounts are only used as context owners in server.
    """

    ACCOUNT = "account"
    ORGANIZATION = "organization"

    def visit(self, account: typing.Callable[[], T_Result], organization: typing.Callable[[], T_Result]) -> T_Result:
        if self is ContextCreateNewContextRequestOwnerIdType.ACCOUNT:
            return account()
        if self is ContextCreateNewContextRequestOwnerIdType.ORGANIZATION:
            return organization()
