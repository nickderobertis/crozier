

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_top_topics_response_topic_list_topics_item_posters_item import (
    ListTopTopicsResponseTopicListTopicsItemPostersItem,
)


class ListTopTopicsResponseTopicListTopicsItem(UniversalBaseModel):
    archetype: typing.Optional[str] = None
    archived: typing.Optional[bool] = None
    bookmarked: typing.Optional[bool] = None
    bumped: typing.Optional[bool] = None
    bumped_at: typing.Optional[str] = None
    category_id: typing.Optional[int] = None
    closed: typing.Optional[bool] = None
    created_at: typing.Optional[str] = None
    fancy_title: typing.Optional[str] = None
    featured_link: typing.Optional[str] = None
    has_summary: typing.Optional[bool] = None
    highest_post_number: typing.Optional[int] = None
    id: typing.Optional[int] = None
    image_url: typing.Optional[str] = None
    last_posted_at: typing.Optional[str] = None
    last_poster_username: typing.Optional[str] = None
    last_read_post_number: typing.Optional[int] = None
    like_count: typing.Optional[int] = None
    liked: typing.Optional[bool] = None
    notification_level: typing.Optional[int] = None
    op_like_count: typing.Optional[int] = None
    pinned: typing.Optional[bool] = None
    pinned_globally: typing.Optional[bool] = None
    posters: typing.Optional[typing.List[ListTopTopicsResponseTopicListTopicsItemPostersItem]] = None
    posts_count: typing.Optional[int] = None
    reply_count: typing.Optional[int] = None
    slug: typing.Optional[str] = None
    title: typing.Optional[str] = None
    unpinned: typing.Optional[bool] = None
    unread_posts: typing.Optional[int] = None
    unseen: typing.Optional[bool] = None
    views: typing.Optional[int] = None
    visible: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
