

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_topic_response_actions_summary_item import GetTopicResponseActionsSummaryItem
from .get_topic_response_details import GetTopicResponseDetails
from .get_topic_response_post_stream import GetTopicResponsePostStream
from .get_topic_response_suggested_topics_item import GetTopicResponseSuggestedTopicsItem
from .get_topic_response_tags_descriptions import GetTopicResponseTagsDescriptions


class GetTopicResponse(UniversalBaseModel):
    actions_summary: typing.List[GetTopicResponseActionsSummaryItem]
    archetype: str
    archived: bool
    bookmarked: bool
    bookmarks: typing.List[typing.Optional[typing.Any]]
    category_id: int
    chunk_size: int
    closed: bool
    created_at: str
    current_post_number: typing.Optional[int] = None
    deleted_at: typing.Optional[str] = None
    deleted_by: typing.Optional[str] = None
    details: GetTopicResponseDetails
    draft: typing.Optional[str] = None
    draft_key: str
    draft_sequence: int
    fancy_title: str
    featured_link: typing.Optional[str] = None
    has_deleted: bool
    has_summary: bool
    highest_post_number: typing.Optional[int] = None
    id: int
    image_url: typing.Optional[str] = None
    last_posted_at: typing.Optional[str] = None
    like_count: int
    message_bus_last_id: int
    participant_count: int
    pinned: bool
    pinned_at: typing.Optional[str] = None
    pinned_globally: bool
    pinned_until: typing.Optional[str] = None
    post_stream: GetTopicResponsePostStream
    posts_count: int
    reply_count: int
    show_read_indicator: bool
    slow_mode_enabled_until: typing.Optional[str] = None
    slow_mode_seconds: int
    slug: str
    suggested_topics: typing.List[GetTopicResponseSuggestedTopicsItem]
    tags: typing.List[typing.Optional[typing.Any]]
    tags_descriptions: GetTopicResponseTagsDescriptions
    thumbnails: typing.Optional[str] = None
    timeline_lookup: typing.List[typing.Optional[typing.Any]]
    title: str
    topic_timer: typing.Optional[str] = None
    unpinned: typing.Optional[str] = None
    user_id: int
    views: int
    visible: bool
    word_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
