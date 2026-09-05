

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .group_first_message import GroupFirstMessage
from .group_properties import GroupProperties
from .user import User


class Group(UniversalBaseModel):
    first_message: typing.Optional[GroupFirstMessage] = None
    id: int
    latest_message: typing.Optional["GroupMessage"] = None
    member_count: typing.Optional[int] = None
    owner: typing.Optional[User] = None
    properties: typing.Optional[GroupProperties] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .group_message import GroupMessage

update_forward_refs(Group, GroupMessage=GroupMessage)
