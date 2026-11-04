

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .workflows_list_approvals_response_approval_groups_item import WorkflowsListApprovalsResponseApprovalGroupsItem
from .workflows_list_approvals_response_roles_item import WorkflowsListApprovalsResponseRolesItem


class WorkflowsListApprovalsResponse(UniversalBaseModel):
    title: typing.Optional[str] = None
    workflow_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="workflowId"), pydantic.Field(alias="workflowId")
    ] = None
    approval_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[WorkflowsListApprovalsResponseApprovalGroupsItem]],
        FieldMetadata(alias="approvalGroups"),
        pydantic.Field(alias="approvalGroups"),
    ] = None
    roles: typing.Optional[typing.List[WorkflowsListApprovalsResponseRolesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
