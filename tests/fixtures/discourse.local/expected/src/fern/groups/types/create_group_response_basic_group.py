

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateGroupResponseBasicGroup(UniversalBaseModel):
    allow_membership_requests: bool
    automatic: bool
    bio_cooked: typing.Optional[str] = None
    bio_excerpt: typing.Optional[str] = None
    bio_raw: typing.Optional[str] = None
    can_admin_group: bool
    can_edit_group: typing.Optional[bool] = None
    can_see_members: bool
    default_notification_level: int
    flair_bg_color: typing.Optional[str] = None
    flair_color: typing.Optional[str] = None
    flair_url: typing.Optional[str] = None
    full_name: typing.Optional[str] = None
    grant_trust_level: typing.Optional[str] = None
    has_messages: bool
    id: int
    incoming_email: typing.Optional[str] = None
    members_visibility_level: int
    membership_request_template: typing.Optional[str] = None
    mentionable_level: int
    messageable_level: int
    name: str
    primary_group: bool
    public_admission: bool
    public_exit: bool
    publish_read_state: bool
    title: typing.Optional[str] = None
    user_count: int
    visibility_level: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
