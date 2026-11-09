

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .webhook_environment_values import WebhookEnvironmentValues


class PendingExpirationWebhook(UniversalBaseModel):
    """
    Fired when an Item’s access consent is expiring in 7 days. Some Items have explicit expiration times and we try to relay this when possible to reduce service disruption. This can be resolved by having the user go through Link’s update mode.
    """

    consent_expiration_time: dt.datetime = pydantic.Field()
    """
    The date and time at which the Item's access consent will expire, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format
    """

    environment: WebhookEnvironmentValues
    item_id: ItemId
    webhook_code: str = pydantic.Field()
    """
    `PENDING_EXPIRATION`
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
