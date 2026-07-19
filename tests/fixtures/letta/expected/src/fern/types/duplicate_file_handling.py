

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DuplicateFileHandling(enum.StrEnum):
    """
    How to handle duplicate filenames when uploading files
    """

    SKIP = "skip"
    ERROR = "error"
    SUFFIX = "suffix"
    REPLACE = "replace"

    def visit(
        self,
        skip: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        suffix: typing.Callable[[], T_Result],
        replace: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DuplicateFileHandling.SKIP:
            return skip()
        if self is DuplicateFileHandling.ERROR:
            return error()
        if self is DuplicateFileHandling.SUFFIX:
            return suffix()
        if self is DuplicateFileHandling.REPLACE:
            return replace()
