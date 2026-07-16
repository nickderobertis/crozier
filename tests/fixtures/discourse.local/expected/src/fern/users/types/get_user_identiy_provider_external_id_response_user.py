

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_identiy_provider_external_id_response_user_custom_fields import (
    GetUserIdentiyProviderExternalIdResponseUserCustomFields,
)
from .get_user_identiy_provider_external_id_response_user_group_users_item import (
    GetUserIdentiyProviderExternalIdResponseUserGroupUsersItem,
)
from .get_user_identiy_provider_external_id_response_user_groups_item import (
    GetUserIdentiyProviderExternalIdResponseUserGroupsItem,
)
from .get_user_identiy_provider_external_id_response_user_user_auth_tokens_item import (
    GetUserIdentiyProviderExternalIdResponseUserUserAuthTokensItem,
)
from .get_user_identiy_provider_external_id_response_user_user_fields import (
    GetUserIdentiyProviderExternalIdResponseUserUserFields,
)
from .get_user_identiy_provider_external_id_response_user_user_notification_schedule import (
    GetUserIdentiyProviderExternalIdResponseUserUserNotificationSchedule,
)
from .get_user_identiy_provider_external_id_response_user_user_option import (
    GetUserIdentiyProviderExternalIdResponseUserUserOption,
)


class GetUserIdentiyProviderExternalIdResponseUser(UniversalBaseModel):
    admin: bool
    allowed_pm_usernames: typing.List[typing.Any]
    avatar_template: str
    badge_count: int
    can_be_deleted: bool
    can_change_bio: bool
    can_change_location: bool
    can_change_tracking_preferences: bool
    can_change_website: bool
    can_delete_all_posts: bool
    can_edit: bool
    can_edit_email: bool
    can_edit_name: bool
    can_edit_username: bool
    can_ignore_user: bool
    can_mute_user: bool
    can_send_private_message_to_user: bool
    can_send_private_messages: bool
    can_upload_profile_header: bool
    can_upload_user_card_background: bool
    created_at: str
    custom_fields: GetUserIdentiyProviderExternalIdResponseUserCustomFields
    featured_topic: typing.Optional[str] = None
    featured_user_badge_ids: typing.List[typing.Any]
    flair_bg_color: typing.Optional[str] = None
    flair_color: typing.Optional[str] = None
    flair_group_id: typing.Optional[str] = None
    flair_name: typing.Optional[str] = None
    flair_url: typing.Optional[str] = None
    group_users: typing.List[GetUserIdentiyProviderExternalIdResponseUserGroupUsersItem]
    groups: typing.List[GetUserIdentiyProviderExternalIdResponseUserGroupsItem]
    has_title_badges: bool
    id: int
    ignored: bool
    ignored_usernames: typing.List[typing.Any]
    invited_by: typing.Optional[str] = None
    last_posted_at: typing.Optional[str] = None
    last_seen_at: typing.Optional[str] = None
    locale: typing.Optional[str] = None
    mailing_list_posts_per_day: int
    moderator: bool
    muted: bool
    muted_category_ids: typing.List[typing.Any]
    muted_tags: typing.List[typing.Any]
    muted_usernames: typing.List[typing.Any]
    name: str
    pending_count: int
    pending_posts_count: typing.Optional[int] = None
    post_count: int
    primary_group_id: typing.Optional[str] = None
    primary_group_name: typing.Optional[str] = None
    profile_view_count: int
    recent_time_read: int
    regular_category_ids: typing.List[typing.Any]
    second_factor_backup_enabled: typing.Optional[bool] = None
    second_factor_enabled: bool
    staged: bool
    system_avatar_template: str
    system_avatar_upload_id: typing.Optional[str] = None
    time_read: int
    title: typing.Optional[str] = None
    tracked_category_ids: typing.List[typing.Any]
    tracked_tags: typing.List[typing.Any]
    trust_level: int
    uploaded_avatar_id: typing.Optional[str] = None
    use_logo_small_as_avatar: bool
    user_api_keys: typing.Optional[str] = None
    user_auth_tokens: typing.List[GetUserIdentiyProviderExternalIdResponseUserUserAuthTokensItem]
    user_fields: typing.Optional[GetUserIdentiyProviderExternalIdResponseUserUserFields] = None
    user_notification_schedule: GetUserIdentiyProviderExternalIdResponseUserUserNotificationSchedule
    user_option: GetUserIdentiyProviderExternalIdResponseUserUserOption
    username: str
    watched_category_ids: typing.List[typing.Any]
    watched_first_post_category_ids: typing.List[typing.Any]
    watched_tags: typing.List[typing.Any]
    watching_first_post_tags: typing.List[typing.Any]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
