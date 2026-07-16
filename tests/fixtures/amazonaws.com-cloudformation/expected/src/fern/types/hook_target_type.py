

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class HookTargetType(str, enum.Enum):
    RESOURCE = "RESOURCE"

    def visit(self, resource: typing.Callable[[], T_Result]) -> T_Result:
        if self is HookTargetType.RESOURCE:
            return resource()
