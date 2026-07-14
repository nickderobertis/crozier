

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_specific_posts_from_topic_response_post_stream import GetSpecificPostsFromTopicResponsePostStream


class GetSpecificPostsFromTopicResponse(UniversalBaseModel):
    id: typing.Optional[int] = None
    post_stream: typing.Optional[GetSpecificPostsFromTopicResponsePostStream] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
