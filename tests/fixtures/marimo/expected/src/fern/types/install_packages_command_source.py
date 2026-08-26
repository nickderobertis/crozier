

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InstallPackagesCommandSource(enum.StrEnum):
    KERNEL = "kernel"
    SERVER = "server"

    def visit(self, kernel: typing.Callable[[], T_Result], server: typing.Callable[[], T_Result]) -> T_Result:
        if self is InstallPackagesCommandSource.KERNEL:
            return kernel()
        if self is InstallPackagesCommandSource.SERVER:
            return server()
