

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StorageEntriesNotificationOp(enum.StrEnum):
    STORAGE_ENTRIES = "storage-entries"

    def visit(self, storage_entries: typing.Callable[[], T_Result]) -> T_Result:
        if self is StorageEntriesNotificationOp.STORAGE_ENTRIES:
            return storage_entries()
