

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileStatus(enum.StrEnum):
    ADDED = "added"
    DELETED = "deleted"
    MODIFIED = "modified"

    def visit(
        self,
        added: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
        modified: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileStatus.ADDED:
            return added()
        if self is FileStatus.DELETED:
            return deleted()
        if self is FileStatus.MODIFIED:
            return modified()
