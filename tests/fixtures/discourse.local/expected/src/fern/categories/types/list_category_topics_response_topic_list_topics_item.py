

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_category_topics_response_topic_list_topics_item_posters_item import (
    ListCategoryTopicsResponseTopicListTopicsItemPostersItem,
)


class ListCategoryTopicsResponseTopicListTopicsItem(UniversalBaseModel):
    archetype: str
    archived: bool
    bookmarked: typing.Optional[str] = None
    bumped: bool
    bumped_at: str
    category_id: int
    closed: bool
    created_at: str
    excerpt: str
    fancy_title: str
    featured_link: typing.Optional[str] = None
    has_summary: bool
    highest_post_number: int
    id: int
    image_url: typing.Optional[str] = None
    last_posted_at: str
    last_poster_username: str
    like_count: int
    liked: typing.Optional[str] = None
    pinned: bool
    pinned_globally: bool
    posters: typing.List[ListCategoryTopicsResponseTopicListTopicsItemPostersItem]
    posts_count: int
    reply_count: int
    slug: str
    title: str
    unpinned: typing.Optional[str] = None
    unseen: bool
    views: int
    visible: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
