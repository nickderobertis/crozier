

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IsFilterSearchTermFilterValueThree(enum.StrEnum):
    MODIFIED = "modified"

    def visit(self, modified: typing.Callable[[], T_Result]) -> T_Result:
        if self is IsFilterSearchTermFilterValueThree.MODIFIED:
            return modified()
