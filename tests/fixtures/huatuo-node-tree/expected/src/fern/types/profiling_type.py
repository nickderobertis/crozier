

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProfilingType(enum.StrEnum):
    CPU = "cpu"
    MEMORY = "memory"

    def visit(self, cpu: typing.Callable[[], T_Result], memory: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProfilingType.CPU:
            return cpu()
        if self is ProfilingType.MEMORY:
            return memory()
