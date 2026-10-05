

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IsFilterSearchTermFilterValueZero(enum.StrEnum):
    ROOT = "root"

    def visit(self, root: typing.Callable[[], T_Result]) -> T_Result:
        if self is IsFilterSearchTermFilterValueZero.ROOT:
            return root()
