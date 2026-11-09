

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .webhook_environment_values import WebhookEnvironmentValues


class ItemLoginRepairedWebhook(UniversalBaseModel):
    """
    Fired when an Item login is repaired and the Item no longer needs to go through update mode. This will occur when the user completed the update mode flow for the Item, either in your application or in another Plaid-connected app. If you have messaging that tells the user to complete the update mode flow (such as in-app banners or out-of-band notifications) you should silence this messaging upon receiving the `LOGIN_REPAIRED` webhook.
    """

    environment: WebhookEnvironmentValues
    item_id: ItemId
    webhook_code: str = pydantic.Field()
    """
    `LOGIN_REPAIRED`
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
