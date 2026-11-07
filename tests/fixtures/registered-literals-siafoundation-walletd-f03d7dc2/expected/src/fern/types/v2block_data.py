

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hash256 import Hash256
from .v2transaction import V2Transaction


class V2BlockData(UniversalBaseModel):
    """
    Additional data present when a block contains v2 transactions.
    """

    height: int
    commitment: Hash256
    transactions: typing.List[V2Transaction]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
