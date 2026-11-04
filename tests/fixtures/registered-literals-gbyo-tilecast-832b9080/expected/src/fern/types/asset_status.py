

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssetStatus(enum.StrEnum):
    UPLOADING = "uploading"
    UPLOADED = "uploaded"
    QUEUED = "queued"
    INSPECTING = "inspecting"
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"
    DELETING = "deleting"
    DELETED = "deleted"

    def visit(
        self,
        uploading: typing.Callable[[], T_Result],
        uploaded: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        inspecting: typing.Callable[[], T_Result],
        processing: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        deleting: typing.Callable[[], T_Result],
        deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssetStatus.UPLOADING:
            return uploading()
        if self is AssetStatus.UPLOADED:
            return uploaded()
        if self is AssetStatus.QUEUED:
            return queued()
        if self is AssetStatus.INSPECTING:
            return inspecting()
        if self is AssetStatus.PROCESSING:
            return processing()
        if self is AssetStatus.READY:
            return ready()
        if self is AssetStatus.FAILED:
            return failed()
        if self is AssetStatus.DELETING:
            return deleting()
        if self is AssetStatus.DELETED:
            return deleted()
