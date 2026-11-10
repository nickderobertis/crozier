

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .webhook_environment_values import WebhookEnvironmentValues


class InitialUpdateWebhook(UniversalBaseModel):
    """
    Fired when an Item's initial transaction pull is completed. Once this webhook has been fired, transaction data for the most recent 30 days can be fetched for the Item. If [Account Select v2](https://plaid.com/docs/link/customization/#account-select) is enabled, this webhook will also be fired if account selections for the Item are updated, with `new_transactions` set to the number of net new transactions pulled after the account selection update.

    This webhook is intended for use with `/transactions/get`; if you are using the newer `/transactions/sync` endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the `SYNC_UPDATES_AVAILABLE` webhook instead.
    """

    environment: WebhookEnvironmentValues
    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error code associated with the webhook.
    """

    item_id: ItemId
    new_transactions: float = pydantic.Field()
    """
    The number of new, unfetched transactions available.
    """

    webhook_code: str = pydantic.Field()
    """
    `INITIAL_UPDATE`
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
