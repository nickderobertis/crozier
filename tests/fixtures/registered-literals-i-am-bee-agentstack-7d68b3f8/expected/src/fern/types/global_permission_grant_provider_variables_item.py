

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GlobalPermissionGrantProviderVariablesItem(enum.StrEnum):
    READ = "read"
    WRITE = "write"
    ALL = "*"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GlobalPermissionGrantProviderVariablesItem.READ:
            return read()
        if self is GlobalPermissionGrantProviderVariablesItem.WRITE:
            return write()
        if self is GlobalPermissionGrantProviderVariablesItem.ALL:
            return all_()
