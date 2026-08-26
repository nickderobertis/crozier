

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PackageManagementConfigManager(enum.StrEnum):
    PIP = "pip"
    PIXI = "pixi"
    POETRY = "poetry"
    RYE = "rye"
    UV = "uv"

    def visit(
        self,
        pip: typing.Callable[[], T_Result],
        pixi: typing.Callable[[], T_Result],
        poetry: typing.Callable[[], T_Result],
        rye: typing.Callable[[], T_Result],
        uv: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PackageManagementConfigManager.PIP:
            return pip()
        if self is PackageManagementConfigManager.PIXI:
            return pixi()
        if self is PackageManagementConfigManager.POETRY:
            return poetry()
        if self is PackageManagementConfigManager.RYE:
            return rye()
        if self is PackageManagementConfigManager.UV:
            return uv()
