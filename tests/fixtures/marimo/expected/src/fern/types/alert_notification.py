

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .alert_notification_op import AlertNotificationOp
from .alert_notification_variant import AlertNotificationVariant


class AlertNotification(UniversalBaseModel):
    """
    User-facing alert message.

        Attributes:
            title: Alert title.
            description: Alert body (may contain HTML).
            variant: Visual variant (e.g., "danger").
    """

    description: str
    op: AlertNotificationOp
    title: str
    variant: typing.Optional[AlertNotificationVariant] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
