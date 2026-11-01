

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchTestResultsV1TestResultsGetRequestIssuesOneItem(enum.StrEnum):
    ANY = "any"

    def visit(self, any: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchTestResultsV1TestResultsGetRequestIssuesOneItem.ANY:
            return any()
