

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetBlock(UniversalBaseModel):
    block_number: str
    difficulty: str
    gas_limit: str
    gas_used: str
    hash: str
    miner: str
    ok: bool
    parent_hash: str
    size_in_bytes: str
    time_stamp: str
    transactions_count: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
