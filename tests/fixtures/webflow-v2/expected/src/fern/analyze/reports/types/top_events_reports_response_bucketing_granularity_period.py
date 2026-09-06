

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TopEventsReportsResponseBucketingGranularityPeriod(enum.StrEnum):
    """
    Bucket size used for this response.
    """

    DAY = "day"

    def visit(self, day: typing.Callable[[], T_Result]) -> T_Result:
        if self is TopEventsReportsResponseBucketingGranularityPeriod.DAY:
            return day()
