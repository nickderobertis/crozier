

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InstallPackagesRequestSource(enum.StrEnum):
    KERNEL = "kernel"
    SERVER = "server"

    def visit(self, kernel: typing.Callable[[], T_Result], server: typing.Callable[[], T_Result]) -> T_Result:
        if self is InstallPackagesRequestSource.KERNEL:
            return kernel()
        if self is InstallPackagesRequestSource.SERVER:
            return server()
