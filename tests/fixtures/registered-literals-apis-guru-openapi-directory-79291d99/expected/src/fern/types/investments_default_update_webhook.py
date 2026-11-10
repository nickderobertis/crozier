

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class InvestmentsDefaultUpdateWebhook(UniversalBaseModel):
    """
    Fired when new transactions have been detected on an investment account.
    """

    canceled_investments_transactions: float = pydantic.Field()
    """
    The number of canceled transactions reported since the last time this webhook was fired.
    """

    environment: WebhookEnvironmentValues
    error: typing.Optional[PlaidError] = None
    item_id: ItemId
    new_investments_transactions: float = pydantic.Field()
    """
    The number of new transactions reported since the last time this webhook was fired.
    """

    webhook_code: str = pydantic.Field()
    """
    `DEFAULT_UPDATE`
    """

    webhook_type: str = pydantic.Field()
    """
    `INVESTMENTS_TRANSACTIONS`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
