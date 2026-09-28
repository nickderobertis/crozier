

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectApprovalOverridesValue(enum.StrEnum):
    AUTO = "auto"
    MANUAL = "manual"

    def visit(self, auto: typing.Callable[[], T_Result], manual: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProjectApprovalOverridesValue.AUTO:
            return auto()
        if self is ProjectApprovalOverridesValue.MANUAL:
            return manual()
