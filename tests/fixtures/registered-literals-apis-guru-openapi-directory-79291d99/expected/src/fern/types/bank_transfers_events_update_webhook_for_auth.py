

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_environment_values import WebhookEnvironmentValues


class BankTransfersEventsUpdateWebhookForAuth(UniversalBaseModel):
    """
    Fired when new ACH events are available. To begin receiving this webhook, you must first register your webhook listener endpoint via the [webhooks page in the Dashboard](https://dashboard.plaid.com/team/webhooks). The `BANK_TRANSFERS_EVENTS_UPDATE` webhook can be used to track the progress of ACH transfers used in [micro-deposit verification](/docs/auth/coverage/microdeposit-events/). Receiving this webhook indicates you should fetch the new events from `/bank_transfer/event/sync`. Note that [Transfer](https://plaid.com/docs/transfer) customers should use Transfer webhooks instead of using `BANK_TRANSFERS_EVENTS_UPDATE`; see [micro-deposit events documentation](https://plaid.com/docs/auth/coverage/microdeposit-events/) for more details.
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
