

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InstallPackagesCommandType(enum.StrEnum):
    INSTALL_PACKAGES = "install-packages"

    def visit(self, install_packages: typing.Callable[[], T_Result]) -> T_Result:
        if self is InstallPackagesCommandType.INSTALL_PACKAGES:
            return install_packages()
