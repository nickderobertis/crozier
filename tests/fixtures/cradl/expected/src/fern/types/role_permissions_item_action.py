

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RolePermissionsItemAction(enum.StrEnum):
    READ = "read"
    WRITE = "write"
    DELEGATE = "delegate"
    ALL = "*"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        delegate: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RolePermissionsItemAction.READ:
            return read()
        if self is RolePermissionsItemAction.WRITE:
            return write()
        if self is RolePermissionsItemAction.DELEGATE:
            return delegate()
        if self is RolePermissionsItemAction.ALL:
            return all_()
