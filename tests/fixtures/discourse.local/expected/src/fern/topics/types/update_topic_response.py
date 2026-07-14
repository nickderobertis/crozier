

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_topic_response_basic_topic import UpdateTopicResponseBasicTopic


class UpdateTopicResponse(UniversalBaseModel):
    basic_topic: typing.Optional[UpdateTopicResponseBasicTopic] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
