

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActActionResponsePolicyStateCode(enum.StrEnum):
    SAFETY_REVIEW_REQUIRED = "safety_review_required"
    AUTHORIZATION_RESTRICTED = "authorization_restricted"
    ACTION_BLOCKED = "action_blocked"

    def visit(
        self,
        safety_review_required: typing.Callable[[], T_Result],
        authorization_restricted: typing.Callable[[], T_Result],
        action_blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActActionResponsePolicyStateCode.SAFETY_REVIEW_REQUIRED:
            return safety_review_required()
        if self is ActActionResponsePolicyStateCode.AUTHORIZATION_RESTRICTED:
            return authorization_restricted()
        if self is ActActionResponsePolicyStateCode.ACTION_BLOCKED:
            return action_blocked()
