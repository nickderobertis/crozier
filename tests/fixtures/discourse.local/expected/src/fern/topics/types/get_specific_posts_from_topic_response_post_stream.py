

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_specific_posts_from_topic_response_post_stream_posts_item import (
    GetSpecificPostsFromTopicResponsePostStreamPostsItem,
)


class GetSpecificPostsFromTopicResponsePostStream(UniversalBaseModel):
    posts: typing.Optional[typing.List[GetSpecificPostsFromTopicResponsePostStreamPostsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
