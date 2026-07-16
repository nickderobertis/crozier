

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_category_response_category_custom_fields import GetCategoryResponseCategoryCustomFields
from .get_category_response_category_group_permissions_item import GetCategoryResponseCategoryGroupPermissionsItem
from .get_category_response_category_required_tag_groups_item import GetCategoryResponseCategoryRequiredTagGroupsItem


class GetCategoryResponseCategory(UniversalBaseModel):
    all_topics_wiki: bool
    allow_badges: bool
    allow_global_tags: typing.Optional[bool] = None
    allow_unlimited_owner_edits_on_first_post: bool
    allowed_tag_groups: typing.Optional[typing.List[typing.Any]] = None
    allowed_tags: typing.Optional[typing.List[typing.Any]] = None
    auto_close_based_on_last_post: bool
    auto_close_hours: typing.Optional[str] = None
    available_groups: typing.List[typing.Any]
    can_delete: bool
    can_edit: bool
    color: str
    custom_fields: GetCategoryResponseCategoryCustomFields
    default_list_filter: str
    default_slow_mode_seconds: typing.Optional[str] = None
    default_top_period: str
    default_view: typing.Optional[str] = None
    description: typing.Optional[str] = None
    description_excerpt: typing.Optional[str] = None
    description_text: typing.Optional[str] = None
    email_in: typing.Optional[str] = None
    email_in_allow_strangers: bool
    form_template_ids: typing.Optional[typing.List[typing.Any]] = None
    group_permissions: typing.List[GetCategoryResponseCategoryGroupPermissionsItem]
    has_children: typing.Optional[str] = None
    id: int
    mailinglist_mirror: bool
    minimum_required_tags: int
    name: str
    navigate_to_first_post_after_read: bool
    notification_level: int
    num_featured_topics: int
    permission: typing.Optional[int] = None
    position: int
    post_count: int
    read_only_banner: typing.Optional[str] = None
    read_restricted: bool
    required_tag_groups: typing.List[GetCategoryResponseCategoryRequiredTagGroupsItem]
    search_priority: int
    show_subcategory_list: bool
    slug: str
    sort_ascending: typing.Optional[str] = None
    sort_order: typing.Optional[str] = None
    subcategory_list_style: str
    text_color: str
    topic_count: int
    topic_featured_link_allowed: bool
    topic_template: typing.Optional[str] = None
    topic_url: typing.Optional[str] = None
    uploaded_background: typing.Optional[str] = None
    uploaded_logo: typing.Optional[str] = None
    uploaded_logo_dark: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
