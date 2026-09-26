

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .http_return_code import HttpReturnCode
from .load_state_collection_partition_data import LoadStateCollectionPartitionData


class LoadStateCollectionPartition(UniversalBaseModel):
    code: HttpReturnCode
    data: LoadStateCollectionPartitionData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
