

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_topic_response_suggested_topics_item_posters_item import GetTopicResponseSuggestedTopicsItemPostersItem
from .get_topic_response_suggested_topics_item_tags_descriptions import (
    GetTopicResponseSuggestedTopicsItemTagsDescriptions,
)


class GetTopicResponseSuggestedTopicsItem(UniversalBaseModel):
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
    highest_post_number: int
    id: int
    image_url: typing.Optional[str] = None
    last_posted_at: typing.Optional[str] = None
    like_count: int
    liked: typing.Optional[str] = None
    pinned: bool
    posters: typing.List[GetTopicResponseSuggestedTopicsItemPostersItem]
    posts_count: int
    reply_count: int
    slug: str
    tags: typing.List[typing.Any]
    tags_descriptions: GetTopicResponseSuggestedTopicsItemTagsDescriptions
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
