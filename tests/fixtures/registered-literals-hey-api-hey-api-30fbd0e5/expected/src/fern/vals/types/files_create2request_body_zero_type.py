

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FilesCreate2RequestBodyZeroType(enum.StrEnum):
    DIRECTORY = "directory"

    def visit(self, directory: typing.Callable[[], T_Result]) -> T_Result:
        if self is FilesCreate2RequestBodyZeroType.DIRECTORY:
            return directory()
