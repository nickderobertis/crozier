

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_all_workflow_approvals_response_approval_groups_item_reviewers_item import (
    ListAllWorkflowApprovalsResponseApprovalGroupsItemReviewersItem,
)


class ListAllWorkflowApprovalsResponseApprovalGroupsItem(UniversalBaseModel):
    reviewers: typing.Optional[typing.List[ListAllWorkflowApprovalsResponseApprovalGroupsItemReviewersItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
