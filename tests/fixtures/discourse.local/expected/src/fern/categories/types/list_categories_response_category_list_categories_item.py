

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListCategoriesResponseCategoryListCategoriesItem(UniversalBaseModel):
    can_edit: bool
    color: str
    default_list_filter: str
    default_top_period: str
    default_view: typing.Optional[str] = None
    description: typing.Optional[str] = None
    description_excerpt: typing.Optional[str] = None
    description_text: typing.Optional[str] = None
    has_children: bool
    id: int
    is_uncategorized: typing.Optional[bool] = None
    minimum_required_tags: int
    name: str
    navigate_to_first_post_after_read: bool
    notification_level: int
    num_featured_topics: int
    permission: int
    position: int
    post_count: int
    read_restricted: bool
    show_subcategory_list: bool
    slug: str
    sort_ascending: typing.Optional[str] = None
    sort_order: typing.Optional[str] = None
    subcategory_ids: typing.List[typing.Any]
    subcategory_list: typing.Optional[typing.List[typing.Any]] = None
    subcategory_list_style: str
    text_color: str
    topic_count: int
    topic_template: typing.Optional[str] = None
    topic_url: typing.Optional[str] = None
    topics_all_time: int
    topics_day: int
    topics_month: int
    topics_week: int
    topics_year: int
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
