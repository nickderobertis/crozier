

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_authorization_decision_rationale_code import TransferAuthorizationDecisionRationaleCode


class TransferAuthorizationDecisionRationale(UniversalBaseModel):
    """
    The rationale for Plaid's decision regarding a proposed transfer. It is always set for `declined` decisions, and may or may not be null for `approved` decisions.
    """

    code: TransferAuthorizationDecisionRationaleCode
    description: str = pydantic.Field()
    """
    A human-readable description of the code associated with a transfer approval or transfer decline.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
