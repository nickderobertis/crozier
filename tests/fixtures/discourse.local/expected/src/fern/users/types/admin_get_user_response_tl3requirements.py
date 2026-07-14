

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .admin_get_user_response_tl3requirements_penalty_counts import AdminGetUserResponseTl3RequirementsPenaltyCounts


class AdminGetUserResponseTl3Requirements(UniversalBaseModel):
    days_visited: int
    max_flagged_by_users: int
    max_flagged_posts: int
    min_days_visited: int
    min_likes_given: int
    min_likes_received: int
    min_likes_received_days: int
    min_likes_received_users: int
    min_posts_read: int
    min_posts_read_all_time: int
    min_topics_replied_to: int
    min_topics_viewed: int
    min_topics_viewed_all_time: int
    num_flagged_by_users: int
    num_flagged_posts: int
    num_likes_given: int
    num_likes_received: int
    num_likes_received_days: int
    num_likes_received_users: int
    num_topics_replied_to: int
    on_grace_period: bool
    penalty_counts: AdminGetUserResponseTl3RequirementsPenaltyCounts
    posts_read: int
    posts_read_all_time: int
    requirements_lost: bool
    requirements_met: bool
    time_period: int
    topics_viewed: int
    topics_viewed_all_time: int
    trust_level_locked: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
