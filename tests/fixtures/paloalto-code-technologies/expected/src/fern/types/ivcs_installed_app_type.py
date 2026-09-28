

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IvcsInstalledAppType(enum.StrEnum):
    VCS_INSTALLED_APP = "VCSInstalledApp"

    def visit(self, vcs_installed_app: typing.Callable[[], T_Result]) -> T_Result:
        if self is IvcsInstalledAppType.VCS_INSTALLED_APP:
            return vcs_installed_app()
