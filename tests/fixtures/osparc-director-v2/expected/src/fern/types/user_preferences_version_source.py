

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserPreferencesVersionSource(enum.StrEnum):
    SERVICE_VERSION = "service-version"
    VERSION_DISPLAY = "version-display"

    def visit(
        self, service_version: typing.Callable[[], T_Result], version_display: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is UserPreferencesVersionSource.SERVICE_VERSION:
            return service_version()
        if self is UserPreferencesVersionSource.VERSION_DISPLAY:
            return version_display()
