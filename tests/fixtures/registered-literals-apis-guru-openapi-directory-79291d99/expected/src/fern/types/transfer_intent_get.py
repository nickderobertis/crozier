

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ach_class import AchClass
from .transfer_amount import TransferAmount
from .transfer_authorization_decision_rationale import TransferAuthorizationDecisionRationale
from .transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecision
from .transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
from .transfer_funding_account_id_response import TransferFundingAccountIdResponse
from .transfer_intent_authorization_decision import TransferIntentAuthorizationDecision
from .transfer_intent_create_mode import TransferIntentCreateMode
from .transfer_intent_create_network import TransferIntentCreateNetwork
from .transfer_intent_get_failure_reason import TransferIntentGetFailureReason
from .transfer_intent_status import TransferIntentStatus
from .transfer_metadata import TransferMetadata
from .transfer_user_in_response import TransferUserInResponse


class TransferIntentGet(UniversalBaseModel):
    """
    Represents a transfer intent within Transfer UI.
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid `account_id` for the account that will be debited or credited. Returned only if `account_id` was set on intent creation.
    """

    ach_class: typing.Optional[AchClass] = None
    amount: TransferAmount
    authorization_decision: typing.Optional[TransferIntentAuthorizationDecision] = None
    authorization_decision_rationale: typing.Optional[TransferAuthorizationDecisionRationale] = None
    created: dt.datetime = pydantic.Field()
    """
    The datetime the transfer was created. This will be of the form `2006-01-02T15:04:05Z`.
    """

    description: str = pydantic.Field()
    """
    A description for the underlying transfer. Maximum of 8 characters.
    """

    failure_reason: typing.Optional[TransferIntentGetFailureReason] = None
    funding_account_id: TransferFundingAccountIdResponse
    guarantee_decision: typing.Optional[TransferAuthorizationGuaranteeDecision] = None
    guarantee_decision_rationale: typing.Optional[TransferAuthorizationGuaranteeDecisionRationale] = None
    id: str = pydantic.Field()
    """
    Plaid's unique identifier for a transfer intent object.
    """

    iso_currency_code: str = pydantic.Field()
    """
    The currency of the transfer amount, e.g. "USD"
    """

    metadata: typing.Optional[TransferMetadata] = None
    mode: TransferIntentCreateMode
    network: typing.Optional[TransferIntentCreateNetwork] = None
    origination_account_id: str = pydantic.Field()
    """
    Plaid’s unique identifier for the origination account used for the transfer.
    """

    require_guarantee: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, the transfer requires a `GUARANTEED` decision by Plaid to proceed (Guarantee customers only).
    """

    status: TransferIntentStatus
    transfer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plaid's unique identifier for the transfer created through the UI. Returned only if the transfer was successfully created. Null value otherwise.
    """

    user: TransferUserInResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
