

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recurring_transfer_nullable import RecurringTransferNullable
from .request_id import RequestId
from .transfer_authorization_decision import TransferAuthorizationDecision
from .transfer_authorization_decision_rationale import TransferAuthorizationDecisionRationale


class TransferRecurringCreateResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/recurring/create`
    """

    decision: TransferAuthorizationDecision
    decision_rationale: typing.Optional[TransferAuthorizationDecisionRationale] = None
    recurring_transfer: typing.Optional[RecurringTransferNullable] = None
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
