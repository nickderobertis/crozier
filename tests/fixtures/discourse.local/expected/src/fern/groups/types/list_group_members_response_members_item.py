

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListGroupMembersResponseMembersItem(UniversalBaseModel):
    added_at: str
    avatar_template: str
    id: int
    last_posted_at: str
    last_seen_at: str
    name: typing.Optional[str] = None
    timezone: str
    title: typing.Optional[str] = None
    username: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
