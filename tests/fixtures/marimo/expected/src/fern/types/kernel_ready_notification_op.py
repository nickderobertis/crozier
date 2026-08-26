

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KernelReadyNotificationOp(enum.StrEnum):
    KERNEL_READY = "kernel-ready"

    def visit(self, kernel_ready: typing.Callable[[], T_Result]) -> T_Result:
        if self is KernelReadyNotificationOp.KERNEL_READY:
            return kernel_ready()
