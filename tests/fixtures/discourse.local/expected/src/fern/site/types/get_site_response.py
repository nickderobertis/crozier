

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_site_response_archetypes_item import GetSiteResponseArchetypesItem
from .get_site_response_categories_item import GetSiteResponseCategoriesItem
from .get_site_response_custom_emoji_translation import GetSiteResponseCustomEmojiTranslation
from .get_site_response_groups_item import GetSiteResponseGroupsItem
from .get_site_response_notification_types import GetSiteResponseNotificationTypes
from .get_site_response_post_action_types_item import GetSiteResponsePostActionTypesItem
from .get_site_response_post_types import GetSiteResponsePostTypes
from .get_site_response_topic_flag_types_item import GetSiteResponseTopicFlagTypesItem
from .get_site_response_trust_levels import GetSiteResponseTrustLevels
from .get_site_response_user_color_schemes_item import GetSiteResponseUserColorSchemesItem
from .get_site_response_user_themes_item import GetSiteResponseUserThemesItem


class GetSiteResponse(UniversalBaseModel):
    anonymous_top_menu_items: typing.List[typing.Any]
    archetypes: typing.List[GetSiteResponseArchetypesItem]
    auth_providers: typing.List[typing.Any]
    can_associate_groups: typing.Optional[bool] = None
    can_create_tag: bool
    can_tag_pms: bool
    can_tag_topics: bool
    categories: typing.List[GetSiteResponseCategoriesItem]
    censored_regexp: typing.List[typing.Dict[str, typing.Any]]
    custom_emoji_translation: GetSiteResponseCustomEmojiTranslation
    default_archetype: str
    default_dark_color_scheme: typing.Optional[typing.Dict[str, typing.Any]] = None
    displayed_about_plugin_stat_groups: typing.Optional[typing.List[typing.Any]] = None
    filters: typing.List[typing.Any]
    groups: typing.List[GetSiteResponseGroupsItem]
    hashtag_configurations: typing.Optional[typing.Dict[str, typing.Any]] = None
    hashtag_icons: typing.Optional[typing.List[typing.Any]] = None
    markdown_additional_options: typing.Optional[typing.Dict[str, typing.Any]] = None
    notification_types: GetSiteResponseNotificationTypes
    periods: typing.List[typing.Any]
    post_action_types: typing.List[GetSiteResponsePostActionTypesItem]
    post_types: GetSiteResponsePostTypes
    show_welcome_topic_banner: typing.Optional[bool] = None
    tags_filter_regexp: str
    top_menu_items: typing.List[typing.Any]
    top_tags: typing.List[typing.Any]
    topic_featured_link_allowed_category_ids: typing.List[typing.Any]
    topic_flag_types: typing.List[GetSiteResponseTopicFlagTypesItem]
    trust_levels: GetSiteResponseTrustLevels
    uncategorized_category_id: int
    user_color_schemes: typing.List[GetSiteResponseUserColorSchemesItem]
    user_field_max_length: int
    user_fields: typing.List[typing.Any]
    user_themes: typing.List[GetSiteResponseUserThemesItem]
    watched_words_link: typing.Optional[str] = None
    watched_words_replace: typing.Optional[str] = None
    whispers_allowed_groups_names: typing.Optional[typing.List[typing.Any]] = None
    wizard_required: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
