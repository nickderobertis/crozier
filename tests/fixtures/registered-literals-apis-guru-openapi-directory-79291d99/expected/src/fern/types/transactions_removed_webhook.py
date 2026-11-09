

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class TransactionsRemovedWebhook(UniversalBaseModel):
    """
    Fired when transaction(s) for an Item are deleted. The deleted transaction IDs are included in the webhook payload. Plaid will typically check for deleted transaction data several times a day.

    This webhook is intended for use with `/transactions/get`; if you are using the newer `/transactions/sync` endpoint, this webhook will still be fired to maintain backwards compatibility, but it is recommended to listen for and respond to the `SYNC_UPDATES_AVAILABLE` webhook instead.
    """

    environment: WebhookEnvironmentValues
    error: typing.Optional[PlaidError] = None
    item_id: ItemId
    removed_transactions: typing.List[str] = pydantic.Field()
    """
    An array of `transaction_ids` corresponding to the removed transactions
    """

    webhook_code: str = pydantic.Field()
    """
    `TRANSACTIONS_REMOVED`
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
