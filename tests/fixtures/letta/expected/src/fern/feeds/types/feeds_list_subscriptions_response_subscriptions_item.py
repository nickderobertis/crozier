

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feeds_list_subscriptions_response_subscriptions_item_merge_strategy import (
    FeedsListSubscriptionsResponseSubscriptionsItemMergeStrategy,
)


class FeedsListSubscriptionsResponseSubscriptionsItem(UniversalBaseModel):
    id: str
    feed_id: str
    agent_id: str
    agent_name: typing.Optional[str] = None
    cron_schedule: str
    merge_strategy: FeedsListSubscriptionsResponseSubscriptionsItemMergeStrategy
    prompt_template: typing.Optional[str] = None
    next_scheduled_at: str
    last_consumed_sequence: float
    last_consumed_at: typing.Optional[str] = None
    disabled_at: typing.Optional[str] = None
    created_at: str
    updated_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
