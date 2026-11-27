

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BenchlingAppManifestAlphaSettingsLifecycleManagement(enum.StrEnum):
    """
    Specify whether app will be activated automatically or manually. If automatic is specified, a webhook url is required.
    """

    AUTOMATIC = "automatic"
    MANUAL = "manual"

    def visit(self, automatic: typing.Callable[[], T_Result], manual: typing.Callable[[], T_Result]) -> T_Result:
        if self is BenchlingAppManifestAlphaSettingsLifecycleManagement.AUTOMATIC:
            return automatic()
        if self is BenchlingAppManifestAlphaSettingsLifecycleManagement.MANUAL:
            return manual()
