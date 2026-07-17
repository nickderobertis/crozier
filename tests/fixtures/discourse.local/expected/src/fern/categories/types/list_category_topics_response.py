

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_category_topics_response_topic_list import ListCategoryTopicsResponseTopicList
from .list_category_topics_response_users_item import ListCategoryTopicsResponseUsersItem


class ListCategoryTopicsResponse(UniversalBaseModel):
    primary_groups: typing.Optional[typing.List[typing.Any]] = None
    topic_list: ListCategoryTopicsResponseTopicList
    users: typing.Optional[typing.List[ListCategoryTopicsResponseUsersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
