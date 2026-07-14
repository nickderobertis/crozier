

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_post_response_actions_summary_item import GetPostResponseActionsSummaryItem


class GetPostResponse(UniversalBaseModel):
    actions_summary: typing.Optional[typing.List[GetPostResponseActionsSummaryItem]] = None
    admin: typing.Optional[bool] = None
    avatar_template: typing.Optional[str] = None
    can_delete: typing.Optional[bool] = None
    can_edit: typing.Optional[bool] = None
    can_recover: typing.Optional[bool] = None
    can_view_edit_history: typing.Optional[bool] = None
    can_wiki: typing.Optional[bool] = None
    cooked: typing.Optional[str] = None
    created_at: typing.Optional[str] = None
    deleted_at: typing.Optional[str] = None
    display_username: typing.Optional[str] = None
    edit_reason: typing.Optional[str] = None
    flair_bg_color: typing.Optional[str] = None
    flair_color: typing.Optional[str] = None
    flair_name: typing.Optional[str] = None
    flair_url: typing.Optional[str] = None
    hidden: typing.Optional[bool] = None
    id: typing.Optional[int] = None
    incoming_link_count: typing.Optional[int] = None
    moderator: typing.Optional[bool] = None
    name: typing.Optional[str] = None
    post_number: typing.Optional[int] = None
    post_type: typing.Optional[int] = None
    primary_group_name: typing.Optional[str] = None
    quote_count: typing.Optional[int] = None
    raw: typing.Optional[str] = None
    readers_count: typing.Optional[int] = None
    reads: typing.Optional[int] = None
    reply_count: typing.Optional[int] = None
    reply_to_post_number: typing.Optional[str] = None
    reviewable_id: typing.Optional[str] = None
    reviewable_score_count: typing.Optional[int] = None
    reviewable_score_pending_count: typing.Optional[int] = None
    score: typing.Optional[int] = None
    staff: typing.Optional[bool] = None
    topic_id: typing.Optional[int] = None
    topic_slug: typing.Optional[str] = None
    trust_level: typing.Optional[int] = None
    updated_at: typing.Optional[str] = None
    user_deleted: typing.Optional[bool] = None
    user_id: typing.Optional[int] = None
    user_title: typing.Optional[str] = None
    username: typing.Optional[str] = None
    version: typing.Optional[int] = None
    wiki: typing.Optional[bool] = None
    yours: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
