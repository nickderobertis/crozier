

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StorageDownloadCommandType(enum.StrEnum):
    STORAGE_DOWNLOAD = "storage-download"

    def visit(self, storage_download: typing.Callable[[], T_Result]) -> T_Result:
        if self is StorageDownloadCommandType.STORAGE_DOWNLOAD:
            return storage_download()
