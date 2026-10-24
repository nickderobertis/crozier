

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rgb_allocation import RgbAllocation
from .utxo import Utxo


class Unspent(UniversalBaseModel):
    utxo: Utxo
    rgb_allocations: typing.List[RgbAllocation]
    pending_blinded: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
