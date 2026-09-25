

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostRolesPermissionsItemAction(enum.StrEnum):
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
        if self is PostRolesPermissionsItemAction.READ:
            return read()
        if self is PostRolesPermissionsItemAction.WRITE:
            return write()
        if self is PostRolesPermissionsItemAction.DELEGATE:
            return delegate()
        if self is PostRolesPermissionsItemAction.ALL:
            return all_()
