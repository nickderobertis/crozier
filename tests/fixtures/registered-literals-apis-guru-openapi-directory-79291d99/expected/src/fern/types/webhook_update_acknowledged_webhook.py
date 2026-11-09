

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class WebhookUpdateAcknowledgedWebhook(UniversalBaseModel):
    """
    Fired when an Item's webhook is updated. This will be sent to the newly specified webhook.
    """

    environment: WebhookEnvironmentValues
    error: typing.Optional[PlaidError] = None
    item_id: ItemId
    new_webhook_url: str = pydantic.Field()
    """
    The new webhook URL
    """

    webhook_code: str = pydantic.Field()
    """
    `WEBHOOK_UPDATE_ACKNOWLEDGED`
    """

    webhook_type: str = pydantic.Field()
    """
    `ITEM`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
