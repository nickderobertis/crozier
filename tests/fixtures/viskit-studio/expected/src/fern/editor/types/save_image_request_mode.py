

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SaveImageRequestMode(enum.StrEnum):
    REPLACE = "replace"
    COPY = "copy"

    def visit(self, replace: typing.Callable[[], T_Result], copy: typing.Callable[[], T_Result]) -> T_Result:
        if self is SaveImageRequestMode.REPLACE:
            return replace()
        if self is SaveImageRequestMode.COPY:
            return copy()
