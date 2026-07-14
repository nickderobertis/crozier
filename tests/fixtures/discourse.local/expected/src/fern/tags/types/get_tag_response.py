

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_tag_response_topic_list import GetTagResponseTopicList
from .get_tag_response_users_item import GetTagResponseUsersItem


class GetTagResponse(UniversalBaseModel):
    primary_groups: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    topic_list: typing.Optional[GetTagResponseTopicList] = None
    users: typing.Optional[typing.List[GetTagResponseUsersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
