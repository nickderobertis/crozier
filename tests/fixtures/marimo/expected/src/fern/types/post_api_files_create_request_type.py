

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiFilesCreateRequestType(enum.StrEnum):
    DIRECTORY = "directory"
    FILE = "file"
    NOTEBOOK = "notebook"

    def visit(
        self,
        directory: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
        notebook: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostApiFilesCreateRequestType.DIRECTORY:
            return directory()
        if self is PostApiFilesCreateRequestType.FILE:
            return file()
        if self is PostApiFilesCreateRequestType.NOTEBOOK:
            return notebook()
