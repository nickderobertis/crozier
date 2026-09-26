

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeStartProfileInstanceRequestStartedByKindOne(enum.StrEnum):
    SYSTEM = "system"

    def visit(self, system: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeStartProfileInstanceRequestStartedByKindOne.SYSTEM:
            return system()
