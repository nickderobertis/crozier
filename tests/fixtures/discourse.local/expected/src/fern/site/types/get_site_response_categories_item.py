

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_site_response_categories_item_required_tag_groups_item import (
    GetSiteResponseCategoriesItemRequiredTagGroupsItem,
)


class GetSiteResponseCategoriesItem(UniversalBaseModel):
    allow_global_tags: bool
    allowed_tag_groups: typing.List[typing.Any]
    allowed_tags: typing.List[typing.Any]
    can_edit: bool
    color: str
    custom_fields: typing.Optional[typing.Dict[str, typing.Any]] = None
    default_list_filter: str
    default_top_period: str
    default_view: typing.Optional[str] = None
    description: typing.Optional[str] = None
    description_excerpt: typing.Optional[str] = None
    description_text: typing.Optional[str] = None
    form_template_ids: typing.Optional[typing.List[typing.Any]] = None
    has_children: bool
    id: int
    minimum_required_tags: int
    name: str
    navigate_to_first_post_after_read: bool
    notification_level: int
    num_featured_topics: int
    parent_category_id: typing.Optional[int] = None
    permission: int
    position: int
    post_count: int
    read_only_banner: typing.Optional[str] = None
    read_restricted: bool
    required_tag_groups: typing.List[GetSiteResponseCategoriesItemRequiredTagGroupsItem]
    show_subcategory_list: bool
    slug: str
    sort_ascending: typing.Optional[str] = None
    sort_order: typing.Optional[str] = None
    subcategory_list_style: str
    text_color: str
    topic_count: int
    topic_template: typing.Optional[str] = None
    topic_url: str
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
