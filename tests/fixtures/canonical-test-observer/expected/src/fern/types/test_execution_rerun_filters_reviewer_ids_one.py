

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TestExecutionRerunFiltersReviewerIdsOne(enum.StrEnum):
    ANY = "any"
    NONE = "none"

    def visit(self, any: typing.Callable[[], T_Result], none: typing.Callable[[], T_Result]) -> T_Result:
        if self is TestExecutionRerunFiltersReviewerIdsOne.ANY:
            return any()
        if self is TestExecutionRerunFiltersReviewerIdsOne.NONE:
            return none()
