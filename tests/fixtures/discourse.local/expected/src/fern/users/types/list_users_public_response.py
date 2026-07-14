

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_users_public_response_directory_items_item import ListUsersPublicResponseDirectoryItemsItem
from .list_users_public_response_meta import ListUsersPublicResponseMeta


class ListUsersPublicResponse(UniversalBaseModel):
    directory_items: typing.List[ListUsersPublicResponseDirectoryItemsItem]
    meta: ListUsersPublicResponseMeta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
