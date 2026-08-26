

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StorageListEntriesCommandType(enum.StrEnum):
    STORAGE_LIST_ENTRIES = "storage-list-entries"

    def visit(self, storage_list_entries: typing.Callable[[], T_Result]) -> T_Result:
        if self is StorageListEntriesCommandType.STORAGE_LIST_ENTRIES:
            return storage_list_entries()
