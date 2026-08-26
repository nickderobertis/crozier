

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileCreateRequestType(enum.StrEnum):
    DIRECTORY = "directory"
    FILE = "file"
    NOTEBOOK = "notebook"

    def visit(
        self,
        directory: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
        notebook: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileCreateRequestType.DIRECTORY:
            return directory()
        if self is FileCreateRequestType.FILE:
            return file()
        if self is FileCreateRequestType.NOTEBOOK:
            return notebook()
