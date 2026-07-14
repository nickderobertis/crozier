

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_sent_private_messages_response_topic_list import GetUserSentPrivateMessagesResponseTopicList
from .get_user_sent_private_messages_response_users_item import GetUserSentPrivateMessagesResponseUsersItem


class GetUserSentPrivateMessagesResponse(UniversalBaseModel):
    primary_groups: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    topic_list: typing.Optional[GetUserSentPrivateMessagesResponseTopicList] = None
    users: typing.Optional[typing.List[GetUserSentPrivateMessagesResponseUsersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
