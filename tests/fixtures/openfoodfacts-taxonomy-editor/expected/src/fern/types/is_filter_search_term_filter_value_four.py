

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IsFilterSearchTermFilterValueFour(enum.StrEnum):
    NOT_MODIFIED = "not:modified"

    def visit(self, not_modified: typing.Callable[[], T_Result]) -> T_Result:
        if self is IsFilterSearchTermFilterValueFour.NOT_MODIFIED:
            return not_modified()
