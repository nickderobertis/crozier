

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeEnvironmentsItemPermission(enum.StrEnum):
    READ = "read"
    WRITE = "write"
    MANAGE = "manage"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        manage: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MeEnvironmentsItemPermission.READ:
            return read()
        if self is MeEnvironmentsItemPermission.WRITE:
            return write()
        if self is MeEnvironmentsItemPermission.MANAGE:
            return manage()
