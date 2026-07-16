

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .admin_get_user_response_approved_by import AdminGetUserResponseApprovedBy
from .admin_get_user_response_groups_item import AdminGetUserResponseGroupsItem
from .admin_get_user_response_penalty_counts import AdminGetUserResponsePenaltyCounts
from .admin_get_user_response_tl3requirements import AdminGetUserResponseTl3Requirements


class AdminGetUserResponse(UniversalBaseModel):
    active: bool
    admin: bool
    api_key_count: int
    approved_by: typing.Optional[AdminGetUserResponseApprovedBy] = None
    associated_accounts: typing.Optional[typing.List[typing.Any]] = None
    avatar_template: str
    badge_count: int
    bounce_score: typing.Optional[int] = None
    can_activate: bool
    can_be_anonymized: bool
    can_be_deleted: bool
    can_be_merged: bool
    can_deactivate: bool
    can_delete_all_posts: bool
    can_delete_sso_record: bool
    can_disable_second_factor: bool
    can_grant_admin: bool
    can_grant_moderation: bool
    can_impersonate: bool
    can_revoke_admin: bool
    can_revoke_moderation: bool
    can_send_activation_email: bool
    can_view_action_logs: bool
    created_at: str
    created_at_age: typing.Optional[float] = None
    days_visited: int
    external_ids: typing.Dict[str, typing.Any]
    flag_level: int
    flags_given_count: int
    flags_received_count: int
    full_suspend_reason: typing.Optional[str] = None
    groups: typing.List[AdminGetUserResponseGroupsItem]
    id: int
    ip_address: str
    last_emailed_age: typing.Optional[float] = None
    last_emailed_at: typing.Optional[str] = None
    last_seen_age: typing.Optional[float] = None
    last_seen_at: typing.Optional[str] = None
    like_count: int
    like_given_count: int
    manual_locked_trust_level: typing.Optional[str] = None
    moderator: bool
    name: typing.Optional[str] = None
    next_penalty: typing.Optional[str] = None
    penalty_counts: typing.Optional[AdminGetUserResponsePenaltyCounts] = None
    post_count: int
    post_edits_count: typing.Optional[int] = None
    posts_read_count: int
    primary_group_id: typing.Optional[str] = None
    private_topics_count: int
    registration_ip_address: typing.Optional[str] = None
    reset_bounce_score_after: typing.Optional[str] = None
    silence_reason: typing.Optional[str] = None
    silenced_by: typing.Optional[str] = None
    single_sign_on_record: typing.Optional[str] = None
    staged: bool
    suspended_by: typing.Optional[str] = None
    time_read: int
    title: typing.Optional[str] = None
    tl3requirements: typing_extensions.Annotated[
        typing.Optional[AdminGetUserResponseTl3Requirements],
        FieldMetadata(alias="tl3_requirements"),
        pydantic.Field(alias="tl3_requirements"),
    ] = None
    topic_count: int
    topics_entered: int
    trust_level: int
    username: str
    warnings_received_count: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
