

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectRequestApprovalOverridesValue(enum.StrEnum):
    AUTO = "auto"
    MANUAL = "manual"
    INHERIT = "inherit"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        manual: typing.Callable[[], T_Result],
        inherit: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectRequestApprovalOverridesValue.AUTO:
            return auto()
        if self is ProjectRequestApprovalOverridesValue.MANUAL:
            return manual()
        if self is ProjectRequestApprovalOverridesValue.INHERIT:
            return inherit()
