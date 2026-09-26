

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v2vectordb_collections_create_response_data import PostV2VectordbCollectionsCreateResponseData


class PostV2VectordbCollectionsCreateResponse(UniversalBaseModel):
    code: typing.Optional[int] = None
    data: typing.Optional[PostV2VectordbCollectionsCreateResponseData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
