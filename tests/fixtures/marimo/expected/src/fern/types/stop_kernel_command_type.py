

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StopKernelCommandType(enum.StrEnum):
    STOP_KERNEL = "stop-kernel"

    def visit(self, stop_kernel: typing.Callable[[], T_Result]) -> T_Result:
        if self is StopKernelCommandType.STOP_KERNEL:
            return stop_kernel()
