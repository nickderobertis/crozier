

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .consensus_v2transaction import ConsensusV2Transaction
from .hash256 import Hash256


class ConsensusV2BlockData(UniversalBaseModel):
    """
    V2-specific block data with consensus transaction information.
    """

    height: int
    commitment: Hash256
    transactions: typing.List[ConsensusV2Transaction]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
