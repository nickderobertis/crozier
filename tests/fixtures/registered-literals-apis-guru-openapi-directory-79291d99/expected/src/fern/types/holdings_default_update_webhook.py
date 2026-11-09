

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class HoldingsDefaultUpdateWebhook(UniversalBaseModel):
    """
    Fired when new or updated holdings have been detected on an investment account. The webhook typically fires in response to any newly added holdings or price changes to existing holdings, most commonly after market close.
    """

    environment: WebhookEnvironmentValues
    error: typing.Optional[PlaidError] = None
    item_id: ItemId
    new_holdings: float = pydantic.Field()
    """
    The number of new holdings reported since the last time this webhook was fired.
    """

    updated_holdings: float = pydantic.Field()
    """
    The number of updated holdings reported since the last time this webhook was fired.
    """

    webhook_code: str = pydantic.Field()
    """
    `DEFAULT_UPDATE`
    """

    webhook_type: str = pydantic.Field()
    """
    `HOLDINGS`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
