

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_user_private_messages_response_topic_list import ListUserPrivateMessagesResponseTopicList
from .list_user_private_messages_response_users_item import ListUserPrivateMessagesResponseUsersItem


class ListUserPrivateMessagesResponse(UniversalBaseModel):
    primary_groups: typing.Optional[typing.List[typing.Any]] = None
    topic_list: typing.Optional[ListUserPrivateMessagesResponseTopicList] = None
    users: typing.Optional[typing.List[ListUserPrivateMessagesResponseUsersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
