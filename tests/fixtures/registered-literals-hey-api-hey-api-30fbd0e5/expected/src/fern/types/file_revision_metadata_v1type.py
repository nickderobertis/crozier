

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileRevisionMetadataV1Type(enum.StrEnum):
    DIRECTORY = "directory"
    FILE = "file"
    INTERVAL = "interval"
    HTTP = "http"
    EMAIL = "email"
    SCRIPT = "script"

    def visit(
        self,
        directory: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
        interval: typing.Callable[[], T_Result],
        http: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        script: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileRevisionMetadataV1Type.DIRECTORY:
            return directory()
        if self is FileRevisionMetadataV1Type.FILE:
            return file()
        if self is FileRevisionMetadataV1Type.INTERVAL:
            return interval()
        if self is FileRevisionMetadataV1Type.HTTP:
            return http()
        if self is FileRevisionMetadataV1Type.EMAIL:
            return email()
        if self is FileRevisionMetadataV1Type.SCRIPT:
            return script()
