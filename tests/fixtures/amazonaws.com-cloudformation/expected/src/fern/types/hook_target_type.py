

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HookTargetType(enum.StrEnum):
    RESOURCE = "RESOURCE"

    def visit(self, resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is HookTargetType.RESOURCE:
            return resource()
