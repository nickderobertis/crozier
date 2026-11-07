

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlobalPermissionGrantProvidersItem(enum.StrEnum):
    READ = "read"
    WRITE = "write"
    ALL = "*"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GlobalPermissionGrantProvidersItem.READ:
            return read()
        if self is GlobalPermissionGrantProvidersItem.WRITE:
            return write()
        if self is GlobalPermissionGrantProvidersItem.ALL:
            return all_()
