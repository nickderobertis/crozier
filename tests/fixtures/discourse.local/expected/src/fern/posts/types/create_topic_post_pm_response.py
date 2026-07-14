

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_topic_post_pm_response_actions_summary_item import CreateTopicPostPmResponseActionsSummaryItem


class CreateTopicPostPmResponse(UniversalBaseModel):
    actions_summary: typing.List[CreateTopicPostPmResponseActionsSummaryItem]
    admin: bool
    avatar_template: str
    bookmarked: bool
    can_delete: bool
    can_edit: bool
    can_recover: bool
    can_view_edit_history: bool
    can_wiki: bool
    cooked: str
    created_at: str
    deleted_at: typing.Optional[str] = None
    display_username: typing.Optional[str] = None
    draft_sequence: int
    edit_reason: typing.Optional[str] = None
    flair_bg_color: typing.Optional[str] = None
    flair_color: typing.Optional[str] = None
    flair_name: typing.Optional[str] = None
    flair_url: typing.Optional[str] = None
    hidden: bool
    id: int
    incoming_link_count: int
    mentioned_users: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    moderator: bool
    name: typing.Optional[str] = None
    post_number: int
    post_type: int
    primary_group_name: typing.Optional[str] = None
    quote_count: int
    raw: typing.Optional[str] = None
    readers_count: int
    reads: int
    reply_count: int
    reply_to_post_number: typing.Optional[str] = None
    reviewable_id: typing.Optional[str] = None
    reviewable_score_count: int
    reviewable_score_pending_count: int
    score: int
    staff: bool
    topic_id: int
    topic_slug: str
    trust_level: int
    updated_at: str
    user_deleted: bool
    user_id: int
    user_title: typing.Optional[str] = None
    username: str
    version: int
    wiki: bool
    yours: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
