

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CatalogCategory(enum.StrEnum):
    VCS = "VCS"
    CI_CD = "CI/CD"
    REGISTRIES = "Registries"
    PRODUCTION = "Production"

    def visit(
        self,
        vcs: typing.Callable[[], T_Result],
        ci_cd: typing.Callable[[], T_Result],
        registries: typing.Callable[[], T_Result],
        production: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CatalogCategory.VCS:
            return vcs()
        if self is CatalogCategory.CI_CD:
            return ci_cd()
        if self is CatalogCategory.REGISTRIES:
            return registries()
        if self is CatalogCategory.PRODUCTION:
            return production()
