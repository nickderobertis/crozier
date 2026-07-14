

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_topic_response_suggested_topics_item_posters_item_user import (
    GetTopicResponseSuggestedTopicsItemPostersItemUser,
)


class GetTopicResponseSuggestedTopicsItemPostersItem(UniversalBaseModel):
    description: str
    extras: str
    user: GetTopicResponseSuggestedTopicsItemPostersItemUser

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
