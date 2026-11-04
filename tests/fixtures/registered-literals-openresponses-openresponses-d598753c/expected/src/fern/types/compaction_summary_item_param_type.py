

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompactionSummaryItemParamType(enum.StrEnum):
    """
    The type of the item. Always `compaction`.
    """

    COMPACTION = "compaction"

    def visit(self, compaction: typing.Callable[[], T_Result]) -> T_Result:
        if self is CompactionSummaryItemParamType.COMPACTION:
            return compaction()
