

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubsctiptionTypeAppPkg(enum.StrEnum):
    """
    'Subscribed notification type'
    """

    APP_PACKAGE_ON_BOARDING = "AppPackageOnBoarding"
    APP_PACAKGE_OPERATION_CHANGE = "AppPacakgeOperationChange"
    APP_PACKAGE_DELETION = "AppPackageDeletion"

    def visit(
        self,
        app_package_on_boarding: typing.Callable[[], T_Result],
        app_pacakge_operation_change: typing.Callable[[], T_Result],
        app_package_deletion: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubsctiptionTypeAppPkg.APP_PACKAGE_ON_BOARDING:
            return app_package_on_boarding()
        if self is SubsctiptionTypeAppPkg.APP_PACAKGE_OPERATION_CHANGE:
            return app_pacakge_operation_change()
        if self is SubsctiptionTypeAppPkg.APP_PACKAGE_DELETION:
            return app_package_deletion()
