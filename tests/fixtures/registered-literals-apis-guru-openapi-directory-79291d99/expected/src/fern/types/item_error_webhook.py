

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class ItemErrorWebhook(UniversalBaseModel):
    """
    Fired when an error is encountered with an Item. The error can be resolved by having the user go through Link’s update mode.
    """

    environment: WebhookEnvironmentValues
    error: typing.Optional[PlaidError] = None
    item_id: ItemId
    webhook_code: str = pydantic.Field()
    """
    `ERROR`
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
