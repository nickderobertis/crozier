

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .webhook_environment_values import WebhookEnvironmentValues


class AutomaticallyVerifiedWebhook(UniversalBaseModel):
    """
    Fired when an Item is verified via automated micro-deposits. We recommend communicating to your users when this event is received to notify them that their account is verified and ready for use.
    """

    account_id: str = pydantic.Field()
    """
    The `account_id` of the account associated with the webhook
    """

    environment: WebhookEnvironmentValues
    item_id: ItemId
    webhook_code: str = pydantic.Field()
    """
    `AUTOMATICALLY_VERIFIED`
    """

    webhook_type: str = pydantic.Field()
    """
    `AUTH`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
