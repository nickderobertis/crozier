

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InstallingPackageAlertNotificationOp(enum.StrEnum):
    INSTALLING_PACKAGE_ALERT = "installing-package-alert"

    def visit(self, installing_package_alert: typing.Callable[[], T_Result]) -> T_Result:
        if self is InstallingPackageAlertNotificationOp.INSTALLING_PACKAGE_ALERT:
            return installing_package_alert()
