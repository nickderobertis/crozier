

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlobalPermissionGrantContextDataItem(enum.StrEnum):
    READ = "read"
    WRITE = "write"
    ALL = "*"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GlobalPermissionGrantContextDataItem.READ:
            return read()
        if self is GlobalPermissionGrantContextDataItem.WRITE:
            return write()
        if self is GlobalPermissionGrantContextDataItem.ALL:
            return all_()
