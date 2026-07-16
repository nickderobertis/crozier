

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppPkgNotificationType(enum.StrEnum):
    """
    Discriminator for the different notification types
    """

    APP_PACKAGE_ON_BOARDED = "AppPackageOnBoarded"
    APP_PACAKGE_ENABLED = "AppPacakgeEnabled"
    APP_PACAKGE_DISABLED = "AppPacakgeDisabled"
    APP_PACKAGE_DELETED = "AppPackageDeleted"

    def visit(
        self,
        app_package_on_boarded: typing.Callable[[], T_Result],
        app_pacakge_enabled: typing.Callable[[], T_Result],
        app_pacakge_disabled: typing.Callable[[], T_Result],
        app_package_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppPkgNotificationType.APP_PACKAGE_ON_BOARDED:
            return app_package_on_boarded()
        if self is AppPkgNotificationType.APP_PACAKGE_ENABLED:
            return app_pacakge_enabled()
        if self is AppPkgNotificationType.APP_PACAKGE_DISABLED:
            return app_pacakge_disabled()
        if self is AppPkgNotificationType.APP_PACKAGE_DELETED:
            return app_package_deleted()
