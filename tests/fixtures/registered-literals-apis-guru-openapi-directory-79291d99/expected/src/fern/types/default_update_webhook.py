

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class DefaultUpdateWebhook(UniversalBaseModel):
    """
    Fired when new transaction data is available for an Item. Plaid will typically check for new transaction data several times a day.

    This webhook is intended for use with `/transactions/get`; if you are using the newer `/transactions/sync` endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the `SYNC_UPDATES_AVAILABLE` webhook instead.
    """

    environment: WebhookEnvironmentValues
    error: typing.Optional[PlaidError] = None
    item_id: str = pydantic.Field()
    """
    The `item_id` of the Item the webhook relates to.
    """

    new_transactions: float = pydantic.Field()
    """
    The number of new transactions detected since the last time this webhook was fired.
    """

    webhook_code: str = pydantic.Field()
    """
    `DEFAULT_UPDATE`
    """

    webhook_type: str = pydantic.Field()
    """
    `TRANSACTIONS`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
