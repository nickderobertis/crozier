

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TagResource20161125RequestOperation(enum.StrEnum):
    TAG = "Tag"

    def visit(self, tag: typing.Callable[[], T_Result]) -> T_Result:
        if self is TagResource20161125RequestOperation.TAG:
            return tag()
