

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_authorization_guarantee_decision_rationale_code import (
    TransferAuthorizationGuaranteeDecisionRationaleCode,
)


class TransferAuthorizationGuaranteeDecisionRationale(UniversalBaseModel):
    """
    The rationale for Plaid's decision to not guarantee a transfer. Will be `null` unless `guarantee_decision` is `NOT_GUARANTEED`.
    """

    code: TransferAuthorizationGuaranteeDecisionRationaleCode
    description: str = pydantic.Field()
    """
    A human-readable description of why the transfer cannot be guaranteed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
