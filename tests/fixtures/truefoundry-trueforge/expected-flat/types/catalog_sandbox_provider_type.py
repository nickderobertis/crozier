

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogSandboxProviderType(enum.StrEnum):
    """
    Daytona sandbox provider.
    """

    DAYTONA = "daytona"

    def visit(self, daytona: typing.Callable[[], T_Result]) -> T_Result:
        if self is CatalogSandboxProviderType.DAYTONA:
            return daytona()
