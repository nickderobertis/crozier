

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bytes import Bytes
from .bytes_max32 import BytesMax32
from .uint256 import Uint256


class StorageProof(UniversalBaseModel):
    key: BytesMax32
    value: Uint256
    proof: typing.List[Bytes]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
