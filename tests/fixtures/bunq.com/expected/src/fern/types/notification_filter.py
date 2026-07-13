

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NotificationFilter(UniversalBaseModel):
    category: typing.Optional[str] = pydantic.Field(default=None)
    """
    The notification category that will match this notification filter. Possible choices are BILLING, CARD_TRANSACTION_FAILED, CARD_TRANSACTION_SUCCESSFUL, CHAT, DRAFT_PAYMENT, IDEAL, SOFORT, MONETARY_ACCOUNT_PROFILE, MUTATION, PAYMENT, PROMOTION, REQUEST, SCHEDULE_RESULT, SCHEDULE_STATUS, SHARE, SUPPORT, TAB_RESULT, USER_APPROVAL.
    """

    notification_delivery_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    The delivery method via which notifications that match this notification filter will be delivered. Possible choices are PUSH for delivery via push notification and URL for delivery via URL callback.
    """

    notification_target: typing.Optional[str] = pydantic.Field(default=None)
    """
    The target of notifications that match this notification filter. For URL notification filters this is the URL to which the callback will be made. For PUSH notifications filters this should always be null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
