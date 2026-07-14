

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_users_public_response_directory_items_item_user import ListUsersPublicResponseDirectoryItemsItemUser


class ListUsersPublicResponseDirectoryItemsItem(UniversalBaseModel):
    days_visited: int
    id: int
    likes_given: int
    likes_received: int
    post_count: int
    posts_read: int
    topic_count: int
    topics_entered: int
    user: ListUsersPublicResponseDirectoryItemsItemUser

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
