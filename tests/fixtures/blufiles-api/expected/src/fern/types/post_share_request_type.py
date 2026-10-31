

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostShareRequestType(enum.StrEnum):
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
        if self is PostShareRequestType.FILE:
            return file()
        if self is PostShareRequestType.FOLDER:
            return folder()
        if self is PostShareRequestType.COLLECTION:
            return collection()
        if self is PostShareRequestType.PASTE:
            return paste()
