

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v2vectordb_partitions_load_response_data import PostV2VectordbPartitionsLoadResponseData


class PostV2VectordbPartitionsLoadResponse(UniversalBaseModel):
    code: int
    data: PostV2VectordbPartitionsLoadResponseData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
