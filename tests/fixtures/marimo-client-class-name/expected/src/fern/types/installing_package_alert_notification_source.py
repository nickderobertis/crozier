

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InstallingPackageAlertNotificationSource(enum.StrEnum):
    KERNEL = "kernel"
    SERVER = "server"

    def visit(self, kernel: typing.Callable[[], T_Result], server: typing.Callable[[], T_Result]) -> T_Result:
        if self is InstallingPackageAlertNotificationSource.KERNEL:
            return kernel()
        if self is InstallingPackageAlertNotificationSource.SERVER:
            return server()
