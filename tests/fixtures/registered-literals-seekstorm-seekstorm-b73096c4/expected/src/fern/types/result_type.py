

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResultType(enum.StrEnum):
    """
    The following result types are supported:
    - **Count** (count all results that match the query, but returning top-k results is not required)
    - **Topk** (returns the top-k results per query, but counting all results that match the query is not required)
    - **TopkCount** (returns the top-k results per query + count all results that match the query)
    """

    COUNT = "Count"
    TOPK = "Topk"
    TOPK_COUNT = "TopkCount"

    def visit(
        self,
        count: typing.Callable[[], T_Result],
        topk: typing.Callable[[], T_Result],
        topk_count: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResultType.COUNT:
            return count()
        if self is ResultType.TOPK:
            return topk()
        if self is ResultType.TOPK_COUNT:
            return topk_count()
