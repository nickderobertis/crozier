

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchTestResultsV1TestResultsGetRequestReviewerIdsOneItem(enum.StrEnum):
    ANY = "any"

    def visit(self, any: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchTestResultsV1TestResultsGetRequestReviewerIdsOneItem.ANY:
            return any()
