

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowsRevertToReviewResponseCode(enum.StrEnum):
    INVALID_PARAM = "INVALID_PARAM"
    INVALID_STATE = "INVALID_STATE"

    def visit(
        self, invalid_param: typing.Callable[[], T_Result], invalid_state: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is WorkflowsRevertToReviewResponseCode.INVALID_PARAM:
            return invalid_param()
        if self is WorkflowsRevertToReviewResponseCode.INVALID_STATE:
            return invalid_state()
