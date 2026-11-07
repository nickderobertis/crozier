

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FileMessage(enum.StrEnum):
    """
    Message in case provided hash not found or error
    """

    NOT_FOUND = "Not found"
    INVALID_KEYS = "Invalid keys"

    def visit(self, not_found: typing.Callable[[], T_Result], invalid_keys: typing.Callable[[], T_Result]) -> T_Result:
        if self is FileMessage.NOT_FOUND:
            return not_found()
        if self is FileMessage.INVALID_KEYS:
            return invalid_keys()
