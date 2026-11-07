

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FilesCreate2RequestBodyOneType(enum.StrEnum):
    FILE = "file"
    INTERVAL = "interval"
    HTTP = "http"
    EMAIL = "email"
    SCRIPT = "script"

    def visit(
        self,
        file: typing.Callable[[], T_Result],
        interval: typing.Callable[[], T_Result],
        http: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        script: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FilesCreate2RequestBodyOneType.FILE:
            return file()
        if self is FilesCreate2RequestBodyOneType.INTERVAL:
            return interval()
        if self is FilesCreate2RequestBodyOneType.HTTP:
            return http()
        if self is FilesCreate2RequestBodyOneType.EMAIL:
            return email()
        if self is FilesCreate2RequestBodyOneType.SCRIPT:
            return script()
