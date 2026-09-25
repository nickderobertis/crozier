

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SandboxProviderManifestType(enum.StrEnum):
    """
    Daytona sandbox provider.
    """

    DAYTONA = "daytona"

    def visit(self, daytona: typing.Callable[[], T_Result]) -> T_Result:
        if self is SandboxProviderManifestType.DAYTONA:
            return daytona()
