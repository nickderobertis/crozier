

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recurring_transfer_id import RecurringTransferId
from .transfer_authorization_decision import TransferAuthorizationDecision
from .transfer_authorization_decision_rationale_code import TransferAuthorizationDecisionRationaleCode
from .webhook_environment_values import WebhookEnvironmentValues


class RecurringTransferSkippedWebhook(UniversalBaseModel):
    """
    Fired when Plaid is unable to originate a new ACH transaction of the recurring transfer on the planned date.
    """

    authorization_decision: TransferAuthorizationDecision
    authorization_decision_rationale_code: typing.Optional[TransferAuthorizationDecisionRationaleCode] = None
    environment: WebhookEnvironmentValues
    recurring_transfer_id: RecurringTransferId
    skipped_origination_date: dt.date = pydantic.Field()
    """
    The planned date on which Plaid is unable to originate a new ACH transaction of the recurring transfer. This will be of the form YYYY-MM-DD.
    """

    webhook_code: str = pydantic.Field()
    """
    `RECURRING_TRANSFER_SKIPPED`
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
