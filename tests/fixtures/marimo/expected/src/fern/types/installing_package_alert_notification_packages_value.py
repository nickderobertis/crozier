

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InstallingPackageAlertNotificationPackagesValue(enum.StrEnum):
    FAILED = "failed"
    INSTALLED = "installed"
    INSTALLING = "installing"
    QUEUED = "queued"

    def visit(
        self,
        failed: typing.Callable[[], T_Result],
        installed: typing.Callable[[], T_Result],
        installing: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InstallingPackageAlertNotificationPackagesValue.FAILED:
            return failed()
        if self is InstallingPackageAlertNotificationPackagesValue.INSTALLED:
            return installed()
        if self is InstallingPackageAlertNotificationPackagesValue.INSTALLING:
            return installing()
        if self is InstallingPackageAlertNotificationPackagesValue.QUEUED:
            return queued()
