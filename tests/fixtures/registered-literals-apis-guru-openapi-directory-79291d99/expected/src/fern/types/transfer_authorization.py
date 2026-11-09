

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_authorization_decision import TransferAuthorizationDecision
from .transfer_authorization_decision_rationale import TransferAuthorizationDecisionRationale
from .transfer_authorization_guarantee_decision import TransferAuthorizationGuaranteeDecision
from .transfer_authorization_guarantee_decision_rationale import TransferAuthorizationGuaranteeDecisionRationale
from .transfer_authorization_id import TransferAuthorizationId
from .transfer_authorization_proposed_transfer import TransferAuthorizationProposedTransfer


class TransferAuthorization(UniversalBaseModel):
    """
    Contains the authorization decision for a proposed transfer.
    """

    created: dt.datetime = pydantic.Field()
    """
    The datetime representing when the authorization was created, in the format `2006-01-02T15:04:05Z`.
    """

    decision: TransferAuthorizationDecision
    decision_rationale: typing.Optional[TransferAuthorizationDecisionRationale] = None
    guarantee_decision: typing.Optional[TransferAuthorizationGuaranteeDecision] = None
    guarantee_decision_rationale: typing.Optional[TransferAuthorizationGuaranteeDecisionRationale] = None
    id: TransferAuthorizationId
    proposed_transfer: TransferAuthorizationProposedTransfer

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
