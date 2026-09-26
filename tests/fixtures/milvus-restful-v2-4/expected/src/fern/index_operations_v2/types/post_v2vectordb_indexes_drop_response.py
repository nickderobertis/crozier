

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v2vectordb_indexes_drop_response_data import PostV2VectordbIndexesDropResponseData


class PostV2VectordbIndexesDropResponse(UniversalBaseModel):
    code: int
    data: PostV2VectordbIndexesDropResponseData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
