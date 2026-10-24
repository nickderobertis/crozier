

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .proposal_capability_block_code import ProposalCapabilityBlockCode


class ProposalCapabilityBlock(UniversalBaseModel):
    code: ProposalCapabilityBlockCode
    message: str
    retryable: bool
    connector_calls: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
