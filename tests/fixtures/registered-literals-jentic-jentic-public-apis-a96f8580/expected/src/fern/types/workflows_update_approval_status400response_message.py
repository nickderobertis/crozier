

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowsUpdateApprovalStatus400ResponseMessage(enum.StrEnum):
    THIS_ROLE_DOES_NOT_EXIST_IN_THIS_WORKFLOW = "This role does not exist in this workflow"
    INVALID_USER_FOR_USER_ATTRIBUTE = "invalid user for user attribute"
    THIS_APPROVAL_EITHER_WAS_NOT_REQUESTED_OR_THIS_USER_WAS_NOT_ASSIGNED_TO_THIS_APPROVAL = (
        "This approval either was not requested or this user was not assigned to this approval"
    )

    def visit(
        self,
        this_role_does_not_exist_in_this_workflow: typing.Callable[[], T_Result],
        invalid_user_for_user_attribute: typing.Callable[[], T_Result],
        this_approval_either_was_not_requested_or_this_user_was_not_assigned_to_this_approval: typing.Callable[
            [], T_Result
        ],
    ) -> T_Result:
        if self is WorkflowsUpdateApprovalStatus400ResponseMessage.THIS_ROLE_DOES_NOT_EXIST_IN_THIS_WORKFLOW:
            return this_role_does_not_exist_in_this_workflow()
        if self is WorkflowsUpdateApprovalStatus400ResponseMessage.INVALID_USER_FOR_USER_ATTRIBUTE:
            return invalid_user_for_user_attribute()
        if (
            self
            is WorkflowsUpdateApprovalStatus400ResponseMessage.THIS_APPROVAL_EITHER_WAS_NOT_REQUESTED_OR_THIS_USER_WAS_NOT_ASSIGNED_TO_THIS_APPROVAL
        ):
            return this_approval_either_was_not_requested_or_this_user_was_not_assigned_to_this_approval()
