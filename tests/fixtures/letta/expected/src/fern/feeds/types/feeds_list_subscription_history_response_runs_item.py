

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feeds_list_subscription_history_response_runs_item_status import (
    FeedsListSubscriptionHistoryResponseRunsItemStatus,
)
from .feeds_list_subscription_history_response_runs_item_type import FeedsListSubscriptionHistoryResponseRunsItemType


class FeedsListSubscriptionHistoryResponseRunsItem(UniversalBaseModel):
    workflow_id: str
    type: FeedsListSubscriptionHistoryResponseRunsItemType
    status: FeedsListSubscriptionHistoryResponseRunsItemStatus
    started_at: str
    completed_at: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
