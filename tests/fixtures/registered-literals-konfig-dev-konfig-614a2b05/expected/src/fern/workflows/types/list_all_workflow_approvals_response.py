

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_all_workflow_approvals_response_approval_groups_item import (
    ListAllWorkflowApprovalsResponseApprovalGroupsItem,
)
from .list_all_workflow_approvals_response_roles_item import ListAllWorkflowApprovalsResponseRolesItem


class ListAllWorkflowApprovalsResponse(UniversalBaseModel):
    workflow_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="workflowId"), pydantic.Field(alias="workflowId")
    ] = None
    title: typing.Optional[str] = None
    approval_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[ListAllWorkflowApprovalsResponseApprovalGroupsItem]],
        FieldMetadata(alias="approvalGroups"),
        pydantic.Field(alias="approvalGroups"),
    ] = None
    roles: typing.Optional[typing.List[ListAllWorkflowApprovalsResponseRolesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
