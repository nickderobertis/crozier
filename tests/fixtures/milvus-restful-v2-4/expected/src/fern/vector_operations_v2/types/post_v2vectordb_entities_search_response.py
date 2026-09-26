

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v2vectordb_entities_search_response_data_item import PostV2VectordbEntitiesSearchResponseDataItem


class PostV2VectordbEntitiesSearchResponse(UniversalBaseModel):
    code: typing.Optional[int] = None
    data: typing.Optional[typing.List[PostV2VectordbEntitiesSearchResponseDataItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
