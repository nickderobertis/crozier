

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchTestResultsV1TestResultsGetRequestAssigneeIdsOneItem(enum.StrEnum):
    ANY = "any"

    def visit(self, any: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchTestResultsV1TestResultsGetRequestAssigneeIdsOneItem.ANY:
            return any()
