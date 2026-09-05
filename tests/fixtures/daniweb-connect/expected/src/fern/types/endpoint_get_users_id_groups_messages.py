

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .api_pagination import ApiPagination


class EndpointGetUsersIdGroupsMessages(UniversalBaseModel):
    data: typing.Optional[typing.List["GroupMessage"]] = None
    pagination: typing.Optional[ApiPagination] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .group import Group
from .group_message import GroupMessage

update_forward_refs(EndpointGetUsersIdGroupsMessages, Group=Group, GroupMessage=GroupMessage)
