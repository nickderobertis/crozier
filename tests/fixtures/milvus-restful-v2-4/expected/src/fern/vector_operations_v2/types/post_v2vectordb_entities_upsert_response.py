

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v2vectordb_entities_upsert_response_data import PostV2VectordbEntitiesUpsertResponseData


class PostV2VectordbEntitiesUpsertResponse(UniversalBaseModel):
    code: typing.Optional[int] = None
    data: typing.Optional[PostV2VectordbEntitiesUpsertResponseData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
