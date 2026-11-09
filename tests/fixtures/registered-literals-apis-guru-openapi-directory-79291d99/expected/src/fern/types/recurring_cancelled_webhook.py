

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recurring_transfer_id import RecurringTransferId
from .webhook_environment_values import WebhookEnvironmentValues


class RecurringCancelledWebhook(UniversalBaseModel):
    """
    Fired when a recurring transfer is cancelled by Plaid.
    """

    environment: WebhookEnvironmentValues
    recurring_transfer_id: RecurringTransferId
    webhook_code: str = pydantic.Field()
    """
    `RECURRING_CANCELLED`
    """

    webhook_type: str = pydantic.Field()
    """
    `TRANSFER`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
