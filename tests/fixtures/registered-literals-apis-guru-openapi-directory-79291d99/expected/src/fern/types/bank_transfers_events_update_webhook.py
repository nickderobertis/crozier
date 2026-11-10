

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_environment_values import WebhookEnvironmentValues


class BankTransfersEventsUpdateWebhook(UniversalBaseModel):
    """
    Fired when new bank transfer events are available. Receiving this webhook indicates you should fetch the new events from `/bank_transfer/event/sync`.
    """

    environment: WebhookEnvironmentValues
    webhook_code: str = pydantic.Field()
    """
    `BANK_TRANSFERS_EVENTS_UPDATE`
    """

    webhook_type: str = pydantic.Field()
    """
    `BANK_TRANSFERS`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
