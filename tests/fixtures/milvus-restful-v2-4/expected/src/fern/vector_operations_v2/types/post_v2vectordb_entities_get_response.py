

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v2vectordb_entities_get_response_data_item import PostV2VectordbEntitiesGetResponseDataItem


class PostV2VectordbEntitiesGetResponse(UniversalBaseModel):
    code: typing.Optional[int] = None
    data: typing.Optional[typing.List[PostV2VectordbEntitiesGetResponseDataItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
