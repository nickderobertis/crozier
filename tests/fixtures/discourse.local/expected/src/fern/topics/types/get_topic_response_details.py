

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_topic_response_details_created_by import GetTopicResponseDetailsCreatedBy
from .get_topic_response_details_last_poster import GetTopicResponseDetailsLastPoster
from .get_topic_response_details_participants_item import GetTopicResponseDetailsParticipantsItem


class GetTopicResponseDetails(UniversalBaseModel):
    can_archive_topic: bool
    can_close_topic: bool
    can_convert_topic: bool
    can_create_post: bool
    can_delete: bool
    can_edit: bool
    can_edit_staff_notes: bool
    can_flag_topic: typing.Optional[bool] = None
    can_invite_to: typing.Optional[bool] = None
    can_invite_via_email: typing.Optional[bool] = None
    can_moderate_category: bool
    can_move_posts: bool
    can_pin_unpin_topic: bool
    can_remove_allowed_users: bool
    can_remove_self_id: int
    can_reply_as_new_topic: bool
    can_review_topic: bool
    can_split_merge_topic: bool
    can_toggle_topic_visibility: bool
    created_by: GetTopicResponseDetailsCreatedBy
    last_poster: GetTopicResponseDetailsLastPoster
    notification_level: int
    participants: typing.Optional[typing.List[GetTopicResponseDetailsParticipantsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
