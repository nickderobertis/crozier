

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LettaUsageStatisticsMessageType(enum.StrEnum):
    USAGE_STATISTICS = "usage_statistics"

    def visit(self, usage_statistics: typing.Callable[[], T_Result]) -> T_Result:
        if self is LettaUsageStatisticsMessageType.USAGE_STATISTICS:
            return usage_statistics()
