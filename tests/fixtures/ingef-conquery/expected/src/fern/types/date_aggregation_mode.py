

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DateAggregationMode(enum.StrEnum):
    """
    Can be used in some queries to alter the way dates are aggregated. Specifically for AND/OR/NEGATION nodes. - NONE will disable date-aggregation, meaning no EVENT_DATES column will be created, - MERGE will union all downstream dates, - INTERSECT will intersect the downstream dates, - LOGICAL depends on the respective nodes: AND will intersect, OR will merge, NEGATION will subtract the dates from ALL-time.
    """

    NONE = "NONE"
    MERGE = "MERGE"
    INTERSECT = "INTERSECT"
    LOGICAL = "LOGICAL"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        merge: typing.Callable[[], T_Result],
        intersect: typing.Callable[[], T_Result],
        logical: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DateAggregationMode.NONE:
            return none()
        if self is DateAggregationMode.MERGE:
            return merge()
        if self is DateAggregationMode.INTERSECT:
            return intersect()
        if self is DateAggregationMode.LOGICAL:
            return logical()
