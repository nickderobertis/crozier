

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflows_list_approvals_response_approval_groups_item_reviewers_item import (
    WorkflowsListApprovalsResponseApprovalGroupsItemReviewersItem,
)


class WorkflowsListApprovalsResponseApprovalGroupsItem(UniversalBaseModel):
    reviewers: typing.Optional[typing.List[WorkflowsListApprovalsResponseApprovalGroupsItemReviewersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
