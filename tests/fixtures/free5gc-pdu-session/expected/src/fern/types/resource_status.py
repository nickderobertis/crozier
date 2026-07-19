

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResourceStatus(enum.StrEnum):
    RELEASED = "RELEASED"

    def visit(self, released: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResourceStatus.RELEASED:
            return released()
