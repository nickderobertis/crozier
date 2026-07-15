

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FileType(str, enum.Enum):
    """
    The type of resource. Could be file, folder or url
    """

    FILE = "file"
    FOLDER = "folder"
    URL = "url"

    def visit(
        self,
        file: typing.Callable[[], T_Result],
        folder: typing.Callable[[], T_Result],
        url: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FileType.FILE:
            return file()
        if self is FileType.FOLDER:
            return folder()
        if self is FileType.URL:
            return url()
