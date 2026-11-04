

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContextPermissionsGrantFilesItem(enum.StrEnum):
    READ = "read"
    WRITE = "write"
    EXTRACT = "extract"
    ALL = "*"

    def visit(
        self,
        read: typing.Callable[[], T_Result],
        write: typing.Callable[[], T_Result],
        extract: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContextPermissionsGrantFilesItem.READ:
            return read()
        if self is ContextPermissionsGrantFilesItem.WRITE:
            return write()
        if self is ContextPermissionsGrantFilesItem.EXTRACT:
            return extract()
        if self is ContextPermissionsGrantFilesItem.ALL:
            return all_()
