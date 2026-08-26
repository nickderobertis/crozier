

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class KernelStartupErrorNotificationOp(enum.StrEnum):
    KERNEL_STARTUP_ERROR = "kernel-startup-error"

    def visit(self, kernel_startup_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is KernelStartupErrorNotificationOp.KERNEL_STARTUP_ERROR:
            return kernel_startup_error()
