

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_group_members_response_members_item import ListGroupMembersResponseMembersItem
from .list_group_members_response_meta import ListGroupMembersResponseMeta
from .list_group_members_response_owners_item import ListGroupMembersResponseOwnersItem


class ListGroupMembersResponse(UniversalBaseModel):
    members: typing.List[ListGroupMembersResponseMembersItem]
    meta: ListGroupMembersResponseMeta
    owners: typing.List[ListGroupMembersResponseOwnersItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
