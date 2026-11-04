

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileStorageType(enum.StrEnum):
    S3 = "s3"
    AZURE = "azure"
    GOOGLE_DRIVE = "google_drive"
    SFTP = "sftp"

    def visit(
        self,
        s3: typing.Callable[[], T_Result],
        azure: typing.Callable[[], T_Result],
        google_drive: typing.Callable[[], T_Result],
        sftp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileStorageType.S3:
            return s3()
        if self is FileStorageType.AZURE:
            return azure()
        if self is FileStorageType.GOOGLE_DRIVE:
            return google_drive()
        if self is FileStorageType.SFTP:
            return sftp()
