

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .installing_package_alert_notification_log_status import InstallingPackageAlertNotificationLogStatus
from .installing_package_alert_notification_op import InstallingPackageAlertNotificationOp
from .installing_package_alert_notification_packages_value import InstallingPackageAlertNotificationPackagesValue
from .installing_package_alert_notification_source import InstallingPackageAlertNotificationSource


class InstallingPackageAlertNotification(UniversalBaseModel):
    """
    Package installation progress with streaming logs.

        Attributes:
            packages: Package name to status (queued/installing/installed/failed).
            logs: Optional streaming logs per package.
            log_status: Log stream status (append/start/done).
            source: Which Python environment packages are installed into.
                    "kernel" (default) installs in the kernel's venv; "server"
                    installs in the server's own Python env.
    """

    log_status: typing.Optional[InstallingPackageAlertNotificationLogStatus] = None
    logs: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    op: InstallingPackageAlertNotificationOp
    packages: typing.Dict[str, InstallingPackageAlertNotificationPackagesValue]
    source: typing.Optional[InstallingPackageAlertNotificationSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
