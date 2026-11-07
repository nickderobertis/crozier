

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ScheduleBulkScanBulkScope(enum.StrEnum):
    FOLDER = "folder"
    UPLOAD = "upload"

    def visit(self, folder: typing.Callable[[], T_Result], upload: typing.Callable[[], T_Result]) -> T_Result:
        if self is ScheduleBulkScanBulkScope.FOLDER:
            return folder()
        if self is ScheduleBulkScanBulkScope.UPLOAD:
            return upload()
