

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StorageDownloadReadyNotificationOp(enum.StrEnum):
    STORAGE_DOWNLOAD_READY = "storage-download-ready"

    def visit(self, storage_download_ready: typing.Callable[[], T_Result]) -> T_Result:
        if self is StorageDownloadReadyNotificationOp.STORAGE_DOWNLOAD_READY:
            return storage_download_ready()
