

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetGroupResponseGroup(UniversalBaseModel):
    allow_membership_requests: bool
    allow_unknown_sender_topic_replies: bool
    associated_group_ids: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    automatic: bool
    automatic_membership_email_domains: typing.Optional[str] = None
    bio_cooked: typing.Optional[str] = None
    bio_excerpt: typing.Optional[str] = None
    bio_raw: typing.Optional[str] = None
    can_admin_group: bool
    can_edit_group: typing.Optional[bool] = None
    can_see_members: bool
    default_notification_level: int
    email_from_alias: typing.Optional[str] = None
    email_password: typing.Optional[str] = None
    email_username: typing.Optional[str] = None
    flair_bg_color: typing.Optional[str] = None
    flair_color: typing.Optional[str] = None
    flair_url: typing.Optional[str] = None
    full_name: typing.Optional[str] = None
    grant_trust_level: typing.Optional[str] = None
    has_messages: bool
    id: int
    imap_enabled: typing.Optional[bool] = None
    imap_last_error: typing.Optional[str] = None
    imap_mailbox_name: str
    imap_mailboxes: typing.List[typing.Optional[typing.Any]]
    imap_new_emails: typing.Optional[str] = None
    imap_old_emails: typing.Optional[str] = None
    imap_port: typing.Optional[str] = None
    imap_server: typing.Optional[str] = None
    imap_ssl: typing.Optional[str] = None
    imap_updated_at: typing.Optional[str] = None
    imap_updated_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    incoming_email: typing.Optional[str] = None
    is_group_owner_display: bool
    is_group_user: bool
    members_visibility_level: int
    membership_request_template: typing.Optional[str] = None
    mentionable: bool
    mentionable_level: int
    message_count: int
    messageable: bool
    messageable_level: int
    muted_category_ids: typing.List[typing.Optional[typing.Any]]
    muted_tags: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    name: str
    primary_group: bool
    public_admission: bool
    public_exit: bool
    publish_read_state: bool
    regular_category_ids: typing.List[typing.Optional[typing.Any]]
    regular_tags: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    smtp_enabled: typing.Optional[bool] = None
    smtp_port: typing.Optional[str] = None
    smtp_server: typing.Optional[str] = None
    smtp_ssl: typing.Optional[str] = None
    smtp_updated_at: typing.Optional[str] = None
    smtp_updated_by: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None
    title: typing.Optional[str] = None
    tracking_category_ids: typing.List[typing.Optional[typing.Any]]
    tracking_tags: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    user_count: int
    visibility_level: int
    watching_category_ids: typing.List[typing.Optional[typing.Any]]
    watching_first_post_category_ids: typing.List[typing.Optional[typing.Any]]
    watching_first_post_tags: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    watching_tags: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
