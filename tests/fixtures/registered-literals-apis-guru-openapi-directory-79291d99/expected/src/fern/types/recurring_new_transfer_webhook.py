

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recurring_transfer_id import RecurringTransferId
from .transfer_id import TransferId
from .webhook_environment_values import WebhookEnvironmentValues


class RecurringNewTransferWebhook(UniversalBaseModel):
    """
    Fired when a new transfer of a recurring transfer is originated.
    """

    environment: WebhookEnvironmentValues
    recurring_transfer_id: RecurringTransferId
    transfer_id: TransferId
    webhook_code: str = pydantic.Field()
    """
    `RECURRING_NEW_TRANSFER`
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
