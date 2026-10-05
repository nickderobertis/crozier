

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IsFilterSearchTermFilterValueTwo(enum.StrEnum):
    NOT_EXTERNAL = "not:external"

    def visit(self, not_external: typing.Callable[[], T_Result]) -> T_Result:
        if self is IsFilterSearchTermFilterValueTwo.NOT_EXTERNAL:
            return not_external()
