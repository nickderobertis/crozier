

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .webhook_environment_values import WebhookEnvironmentValues


class RecurringTransactionsUpdateWebhook(UniversalBaseModel):
    """
    Fired when recurring transactions data is updated. This includes when a new recurring stream is detected or when a new transaction is added to an existing recurring stream. The `RECURRING_TRANSACTIONS_UPDATE` webhook will also fire when one or more attributes of the recurring stream changes, which is usually a result of the addition, update, or removal of transactions to the stream.

    After receipt of this webhook, the updated data can be fetched from `/transactions/recurring/get`.
    """

    account_ids: typing.List[str] = pydantic.Field()
    """
    A list of `account_ids` for accounts that have new or updated recurring transactions data.
    """

    environment: WebhookEnvironmentValues
    item_id: ItemId
    webhook_code: str = pydantic.Field()
    """
    `RECURRING_TRANSACTIONS_UPDATE`
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
