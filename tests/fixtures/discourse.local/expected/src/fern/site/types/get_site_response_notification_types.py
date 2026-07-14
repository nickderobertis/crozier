

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetSiteResponseNotificationTypes(UniversalBaseModel):
    assigned: typing.Optional[int] = None
    bookmark_reminder: int
    chat_group_mention: int
    chat_invitation: int
    chat_mention: int
    chat_message: int
    chat_quoted: typing.Optional[int] = None
    circles_activity: typing.Optional[int] = None
    code_review_commit_approved: int
    custom: int
    edited: int
    event_invitation: int
    event_reminder: int
    following: typing.Optional[int] = None
    following_created_topic: typing.Optional[int] = None
    following_replied: typing.Optional[int] = None
    granted_badge: int
    group_mentioned: int
    group_message_summary: int
    invited_to_private_message: int
    invited_to_topic: int
    invitee_accepted: int
    liked: int
    liked_consolidated: int
    linked: int
    membership_request_accepted: int
    membership_request_consolidated: int
    mentioned: int
    moved_post: int
    new_features: typing.Optional[int] = None
    post_approved: int
    posted: int
    private_message: int
    question_answer_user_commented: typing.Optional[int] = None
    quoted: int
    reaction: int
    replied: int
    topic_reminder: int
    votes_released: int
    watching_category_or_tag: int
    watching_first_post: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
