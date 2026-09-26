

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v2vectordb_indexes_describe_response_data_item import PostV2VectordbIndexesDescribeResponseDataItem


class PostV2VectordbIndexesDescribeResponse(UniversalBaseModel):
    code: int
    data: typing.List[PostV2VectordbIndexesDescribeResponseDataItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
