

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AdminListUsersResponseItem(UniversalBaseModel):
    active: bool
    admin: bool
    avatar_template: str
    created_at: str
    created_at_age: typing.Optional[float] = None
    days_visited: int
    email: typing.Optional[str] = None
    flag_level: int
    id: int
    last_emailed_age: typing.Optional[float] = None
    last_emailed_at: typing.Optional[str] = None
    last_seen_age: typing.Optional[float] = None
    last_seen_at: typing.Optional[str] = None
    manual_locked_trust_level: typing.Optional[str] = None
    moderator: bool
    name: typing.Optional[str] = None
    post_count: int
    posts_read_count: int
    secondary_emails: typing.Optional[typing.List[typing.Any]] = None
    staged: bool
    time_read: int
    title: typing.Optional[str] = None
    topics_entered: int
    trust_level: int
    username: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
