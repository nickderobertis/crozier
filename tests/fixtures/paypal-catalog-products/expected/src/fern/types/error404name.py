

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error404Name(enum.StrEnum):
    RESOURCE_NOT_FOUND = "RESOURCE_NOT_FOUND"

    def visit(self, resource_not_found: typing.Callable[[], T_Result]) -> T_Result:
        if self is Error404Name.RESOURCE_NOT_FOUND:
            return resource_not_found()
