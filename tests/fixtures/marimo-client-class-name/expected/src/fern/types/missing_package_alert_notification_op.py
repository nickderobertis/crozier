

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MissingPackageAlertNotificationOp(enum.StrEnum):
    MISSING_PACKAGE_ALERT = "missing-package-alert"

    def visit(self, missing_package_alert: typing.Callable[[], T_Result]) -> T_Result:
        if self is MissingPackageAlertNotificationOp.MISSING_PACKAGE_ALERT:
            return missing_package_alert()
