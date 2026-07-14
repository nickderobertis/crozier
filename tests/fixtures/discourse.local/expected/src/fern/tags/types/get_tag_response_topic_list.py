

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_tag_response_topic_list_tags_item import GetTagResponseTopicListTagsItem
from .get_tag_response_topic_list_topics_item import GetTagResponseTopicListTopicsItem


class GetTagResponseTopicList(UniversalBaseModel):
    can_create_topic: typing.Optional[bool] = None
    draft: typing.Optional[str] = None
    draft_key: typing.Optional[str] = None
    draft_sequence: typing.Optional[int] = None
    per_page: typing.Optional[int] = None
    tags: typing.Optional[typing.List[GetTagResponseTopicListTagsItem]] = None
    topics: typing.Optional[typing.List[GetTagResponseTopicListTopicsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
