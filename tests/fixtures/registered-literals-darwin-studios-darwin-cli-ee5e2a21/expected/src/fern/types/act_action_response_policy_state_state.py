

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ActActionResponsePolicyStateState(enum.StrEnum):
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    RESTRICTED = "RESTRICTED"
    BLOCKED = "BLOCKED"

    def visit(
        self,
        review_required: typing.Callable[[], T_Result],
        restricted: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActActionResponsePolicyStateState.REVIEW_REQUIRED:
            return review_required()
        if self is ActActionResponsePolicyStateState.RESTRICTED:
            return restricted()
        if self is ActActionResponsePolicyStateState.BLOCKED:
            return blocked()
