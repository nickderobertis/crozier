

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .banner_notification_action import BannerNotificationAction
from .banner_notification_op import BannerNotificationOp
from .banner_notification_variant import BannerNotificationVariant


class BannerNotification(UniversalBaseModel):
    """
    Persistent banner message at top of notebook.

        Attributes:
            title: Banner title.
            description: Banner body (may contain HTML).
            variant: Visual variant (e.g., "danger").
            action: Optional user action (e.g., "restart").
    """

    action: typing.Optional[BannerNotificationAction] = None
    description: str
    op: BannerNotificationOp
    title: str
    variant: typing.Optional[BannerNotificationVariant] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
