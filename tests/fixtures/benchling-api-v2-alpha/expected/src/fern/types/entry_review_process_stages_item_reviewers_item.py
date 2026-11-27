

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .entry_review_process_stages_item_reviewers_item_status import EntryReviewProcessStagesItemReviewersItemStatus
from .party_summary import PartySummary


class EntryReviewProcessStagesItemReviewersItem(PartySummary):
    status: typing.Optional[EntryReviewProcessStagesItemReviewersItemStatus] = pydantic.Field(default=None)
    """
    Status of the Reviewer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
