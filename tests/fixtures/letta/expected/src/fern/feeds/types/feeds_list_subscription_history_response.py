

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .feeds_list_subscription_history_response_runs_item import FeedsListSubscriptionHistoryResponseRunsItem


class FeedsListSubscriptionHistoryResponse(UniversalBaseModel):
    runs: typing.List[FeedsListSubscriptionHistoryResponseRunsItem]
    next_page_token: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
