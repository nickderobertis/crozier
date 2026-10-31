

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FilteredShareType(enum.StrEnum):
    FILE = "file"
    FOLDER = "folder"
    COLLECTION = "collection"
    PASTE = "paste"

    def visit(
        self,
        file: typing.Callable[[], T_Result],
        folder: typing.Callable[[], T_Result],
        collection: typing.Callable[[], T_Result],
        paste: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FilteredShareType.FILE:
            return file()
        if self is FilteredShareType.FOLDER:
            return folder()
        if self is FilteredShareType.COLLECTION:
            return collection()
        if self is FilteredShareType.PASTE:
            return paste()
