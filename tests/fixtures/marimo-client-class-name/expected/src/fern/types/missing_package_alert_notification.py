

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .missing_package_alert_notification_op import MissingPackageAlertNotificationOp
from .missing_package_alert_notification_source import MissingPackageAlertNotificationSource


class MissingPackageAlertNotification(UniversalBaseModel):
    """
    Alert for missing packages with install option.

        Attributes:
            packages: Missing package names.
            isolated: Whether auto-install is possible in this environment.
            source: Which Python environment to install into. "kernel" (default)
                    installs in the kernel's venv; "server" installs in the
                    server's own Python env (e.g. for formatter tools like ruff).
    """

    isolated: bool
    op: MissingPackageAlertNotificationOp
    packages: typing.List[str]
    source: typing.Optional[MissingPackageAlertNotificationSource] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
