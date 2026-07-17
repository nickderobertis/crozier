

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetUserIdentiyProviderExternalIdResponseUserUserOption(UniversalBaseModel):
    allow_private_messages: bool
    auto_track_topics_after_msecs: int
    automatically_unpin_topics: bool
    bookmark_auto_delete_preference: typing.Optional[int] = None
    color_scheme_id: typing.Optional[str] = None
    dark_scheme_id: typing.Optional[str] = None
    default_calendar: typing.Optional[str] = None
    digest_after_minutes: int
    dynamic_favicon: bool
    email_digests: bool
    email_in_reply_to: bool
    email_level: int
    email_messages_level: int
    email_previous_replies: int
    enable_allowed_pm_users: bool
    enable_defer: bool
    enable_quoting: bool
    external_links_in_new_tab: bool
    hide_profile_and_presence: bool
    homepage_id: typing.Optional[str] = None
    include_tl0in_digests: typing_extensions.Annotated[
        bool, FieldMetadata(alias="include_tl0_in_digests"), pydantic.Field(alias="include_tl0_in_digests")
    ]
    like_notification_frequency: int
    mailing_list_mode: bool
    mailing_list_mode_frequency: int
    new_topic_duration_minutes: int
    notification_level_when_replying: int
    oldest_search_log_date: typing.Optional[str] = None
    seen_popups: typing.Optional[typing.List[typing.Any]] = None
    sidebar_list_destination: typing.Optional[str] = None
    skip_new_user_tips: bool
    text_size: str
    text_size_seq: int
    theme_ids: typing.List[typing.Any]
    theme_key_seq: int
    timezone: typing.Optional[str] = None
    title_count_mode: str
    user_id: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
