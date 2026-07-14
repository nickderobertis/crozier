

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_category_topics_response_topic_list_topics_item import ListCategoryTopicsResponseTopicListTopicsItem


class ListCategoryTopicsResponseTopicList(UniversalBaseModel):
    can_create_topic: bool
    per_page: int
    top_tags: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    topics: typing.List[ListCategoryTopicsResponseTopicListTopicsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
