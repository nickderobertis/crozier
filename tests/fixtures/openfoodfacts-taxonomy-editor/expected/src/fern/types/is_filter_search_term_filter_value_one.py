

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IsFilterSearchTermFilterValueOne(enum.StrEnum):
    EXTERNAL = "external"

    def visit(self, external: typing.Callable[[], T_Result]) -> T_Result:
        if self is IsFilterSearchTermFilterValueOne.EXTERNAL:
            return external()
