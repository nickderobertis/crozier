

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BadRequestErrorWorkflowLaunchCode(enum.StrEnum):
    """
    A unique code to identify why the workflow cannot be launched.
    """

    MISSING_PARAM = "MISSING_PARAM"
    INVALID_PARAM = "INVALID_PARAM"
    INVALID_STATE = "INVALID_STATE"

    def visit(
        self,
        missing_param: typing.Callable[[], T_Result],
        invalid_param: typing.Callable[[], T_Result],
        invalid_state: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BadRequestErrorWorkflowLaunchCode.MISSING_PARAM:
            return missing_param()
        if self is BadRequestErrorWorkflowLaunchCode.INVALID_PARAM:
            return invalid_param()
        if self is BadRequestErrorWorkflowLaunchCode.INVALID_STATE:
            return invalid_state()
