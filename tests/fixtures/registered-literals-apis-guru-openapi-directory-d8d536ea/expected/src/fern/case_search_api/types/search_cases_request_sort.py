

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SearchCasesRequestSort(enum.StrEnum):
    FILED_DATE = "filedDate"
    RELEVANCY = "relevancy"

    def visit(self, filed_date: typing.Callable[[], T_Result], relevancy: typing.Callable[[], T_Result]) -> T_Result:
        if self is SearchCasesRequestSort.FILED_DATE:
            return filed_date()
        if self is SearchCasesRequestSort.RELEVANCY:
            return relevancy()
