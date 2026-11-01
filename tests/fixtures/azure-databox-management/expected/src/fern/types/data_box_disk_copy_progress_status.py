

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataBoxDiskCopyProgressStatus(enum.StrEnum):
    """
    The Status of the copy
    """

    NOT_STARTED = "NotStarted"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    COMPLETED_WITH_ERRORS = "CompletedWithErrors"
    FAILED = "Failed"
    NOT_RETURNED = "NotReturned"
    HARDWARE_ERROR = "HardwareError"
    DEVICE_FORMATTED = "DeviceFormatted"
    DEVICE_METADATA_MODIFIED = "DeviceMetadataModified"
    STORAGE_ACCOUNT_NOT_ACCESSIBLE = "StorageAccountNotAccessible"
    UNSUPPORTED_DATA = "UnsupportedData"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        completed_with_errors: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        not_returned: typing.Callable[[], T_Result],
        hardware_error: typing.Callable[[], T_Result],
        device_formatted: typing.Callable[[], T_Result],
        device_metadata_modified: typing.Callable[[], T_Result],
        storage_account_not_accessible: typing.Callable[[], T_Result],
        unsupported_data: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DataBoxDiskCopyProgressStatus.NOT_STARTED:
            return not_started()
        if self is DataBoxDiskCopyProgressStatus.IN_PROGRESS:
            return in_progress()
        if self is DataBoxDiskCopyProgressStatus.COMPLETED:
            return completed()
        if self is DataBoxDiskCopyProgressStatus.COMPLETED_WITH_ERRORS:
            return completed_with_errors()
        if self is DataBoxDiskCopyProgressStatus.FAILED:
            return failed()
        if self is DataBoxDiskCopyProgressStatus.NOT_RETURNED:
            return not_returned()
        if self is DataBoxDiskCopyProgressStatus.HARDWARE_ERROR:
            return hardware_error()
        if self is DataBoxDiskCopyProgressStatus.DEVICE_FORMATTED:
            return device_formatted()
        if self is DataBoxDiskCopyProgressStatus.DEVICE_METADATA_MODIFIED:
            return device_metadata_modified()
        if self is DataBoxDiskCopyProgressStatus.STORAGE_ACCOUNT_NOT_ACCESSIBLE:
            return storage_account_not_accessible()
        if self is DataBoxDiskCopyProgressStatus.UNSUPPORTED_DATA:
            return unsupported_data()
