

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeStartProfileInstanceRequestSourceTwo(enum.StrEnum):
    SCHEDULE = "schedule"

    def visit(self, schedule: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeStartProfileInstanceRequestSourceTwo.SCHEDULE:
            return schedule()
