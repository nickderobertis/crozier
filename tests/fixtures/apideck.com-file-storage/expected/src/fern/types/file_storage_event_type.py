

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FileStorageEventType(str, enum.Enum):
    ALL = "*"
    FILE_STORAGE_FILE_CREATED = "file-storage.file.created"
    FILE_STORAGE_FILE_UPDATED = "file-storage.file.updated"
    FILE_STORAGE_FILE_DELETED = "file-storage.file.deleted"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        file_storage_file_created: typing.Callable[[], T_Result],
        file_storage_file_updated: typing.Callable[[], T_Result],
        file_storage_file_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileStorageEventType.ALL:
            return all_()
        if self is FileStorageEventType.FILE_STORAGE_FILE_CREATED:
            return file_storage_file_created()
        if self is FileStorageEventType.FILE_STORAGE_FILE_UPDATED:
            return file_storage_file_updated()
        if self is FileStorageEventType.FILE_STORAGE_FILE_DELETED:
            return file_storage_file_deleted()
