

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileDownloadTarget(enum.StrEnum):
    WEBSITE = "website"
    S3 = "s3"
    AZURE = "azure"
    GOOGLE_DRIVE = "google_drive"
    SFTP = "sftp"

    def visit(
        self,
        website: typing.Callable[[], T_Result],
        s3: typing.Callable[[], T_Result],
        azure: typing.Callable[[], T_Result],
        google_drive: typing.Callable[[], T_Result],
        sftp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileDownloadTarget.WEBSITE:
            return website()
        if self is FileDownloadTarget.S3:
            return s3()
        if self is FileDownloadTarget.AZURE:
            return azure()
        if self is FileDownloadTarget.GOOGLE_DRIVE:
            return google_drive()
        if self is FileDownloadTarget.SFTP:
            return sftp()
