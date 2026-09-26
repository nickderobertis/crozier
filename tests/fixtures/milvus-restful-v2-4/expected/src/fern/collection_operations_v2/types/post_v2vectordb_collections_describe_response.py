

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v2vectordb_collections_describe_response_data import PostV2VectordbCollectionsDescribeResponseData


class PostV2VectordbCollectionsDescribeResponse(UniversalBaseModel):
    code: int
    data: PostV2VectordbCollectionsDescribeResponseData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
