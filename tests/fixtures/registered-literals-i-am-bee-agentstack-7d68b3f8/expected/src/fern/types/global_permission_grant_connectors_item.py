

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlobalPermissionGrantConnectorsItem(enum.StrEnum):
    READ = "read"
    WRITE = "write"
    PROXY = "proxy"
    ALL = "*"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        proxy: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GlobalPermissionGrantConnectorsItem.READ:
            return read()
        if self is GlobalPermissionGrantConnectorsItem.WRITE:
            return write()
        if self is GlobalPermissionGrantConnectorsItem.PROXY:
            return proxy()
        if self is GlobalPermissionGrantConnectorsItem.ALL:
            return all_()
