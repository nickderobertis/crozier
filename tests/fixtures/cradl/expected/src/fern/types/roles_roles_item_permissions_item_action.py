

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RolesRolesItemPermissionsItemAction(enum.StrEnum):
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
        if self is RolesRolesItemPermissionsItemAction.READ:
            return read()
        if self is RolesRolesItemPermissionsItemAction.WRITE:
            return write()
        if self is RolesRolesItemPermissionsItemAction.DELEGATE:
            return delegate()
        if self is RolesRolesItemPermissionsItemAction.ALL:
            return all_()
