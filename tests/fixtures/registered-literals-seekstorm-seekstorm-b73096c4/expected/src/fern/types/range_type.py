

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RangeType(enum.StrEnum):
    """
    Create query_list and non_unique_query_list
    blockwise intersection : if the corresponding blocks with a 65k docid range for each term have at least a single docid,
    then the intersect_docid within a single block is executed  (=segments?)
    specifies how to count the frequency of numerical facet field values
    """

    COUNT_WITHIN_RANGE = "CountWithinRange"
    COUNT_ABOVE_RANGE = "CountAboveRange"
    COUNT_BELOW_RANGE = "CountBelowRange"

    def visit(
        self,
        count_within_range: typing.Callable[[], T_Result],
        count_above_range: typing.Callable[[], T_Result],
        count_below_range: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RangeType.COUNT_WITHIN_RANGE:
            return count_within_range()
        if self is RangeType.COUNT_ABOVE_RANGE:
            return count_above_range()
        if self is RangeType.COUNT_BELOW_RANGE:
            return count_below_range()
