

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_tags_search_request_target_entity import PostTagsSearchRequestTargetEntity


class PostTagsSearchRequestTarget(UniversalBaseModel):
    entity: PostTagsSearchRequestTargetEntity
    target: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
