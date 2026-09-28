

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverImportRequestSource(enum.StrEnum):
    DISK = "disk"

    def visit(self, disk: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutMockserverImportRequestSource.DISK:
            return disk()
