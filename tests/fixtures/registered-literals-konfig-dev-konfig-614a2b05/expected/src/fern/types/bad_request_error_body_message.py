

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadRequestErrorBodyMessage(enum.StrEnum):
    INVALID_USER_FOR_USER_ATTRIBUTE = "invalid user for user attribute"
    WORKFLOW_WAS_NOT_BUILT_IN_WORKFLOW_DESIGNER_AND_CANNOT_BE_REVERTED_TO_REVIEW_VIA_THE_API = (
        "workflow was not built in workflow designer and cannot be reverted to review via the API"
    )
    WORKFLOW_CANNOT_BE_REVERTED_TO_REVIEW_AS_IT_IS_NOT_IN_THE_SIGN_STAGE = (
        "workflow cannot be reverted to review as it is not in the sign stage"
    )
    VARIOUS_MALFORMED_USER_PAYLOAD_MESSAGES = "various malformed user payload messages"

    def visit(
        self,
        invalid_user_for_user_attribute: typing.Callable[[], T_Result],
        workflow_was_not_built_in_workflow_designer_and_cannot_be_reverted_to_review_via_the_api: typing.Callable[
            [], T_Result
        ],
        workflow_cannot_be_reverted_to_review_as_it_is_not_in_the_sign_stage: typing.Callable[[], T_Result],
        various_malformed_user_payload_messages: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BadRequestErrorBodyMessage.INVALID_USER_FOR_USER_ATTRIBUTE:
            return invalid_user_for_user_attribute()
        if (
            self
            is BadRequestErrorBodyMessage.WORKFLOW_WAS_NOT_BUILT_IN_WORKFLOW_DESIGNER_AND_CANNOT_BE_REVERTED_TO_REVIEW_VIA_THE_API
        ):
            return workflow_was_not_built_in_workflow_designer_and_cannot_be_reverted_to_review_via_the_api()
        if self is BadRequestErrorBodyMessage.WORKFLOW_CANNOT_BE_REVERTED_TO_REVIEW_AS_IT_IS_NOT_IN_THE_SIGN_STAGE:
            return workflow_cannot_be_reverted_to_review_as_it_is_not_in_the_sign_stage()
        if self is BadRequestErrorBodyMessage.VARIOUS_MALFORMED_USER_PAYLOAD_MESSAGES:
            return various_malformed_user_payload_messages()
