

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchTestResultsV1TestResultsGetRequestIssuesTwoItem(enum.StrEnum):
    NONE = "none"

    def visit(self, none: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchTestResultsV1TestResultsGetRequestIssuesTwoItem.NONE:
            return none()
