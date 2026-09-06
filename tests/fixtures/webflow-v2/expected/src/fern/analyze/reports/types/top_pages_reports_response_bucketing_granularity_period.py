

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TopPagesReportsResponseBucketingGranularityPeriod(enum.StrEnum):
    """
    Bucket size used for this response.
    """

    DAY = "day"

    def visit(self, day: typing.Callable[[], T_Result]) -> T_Result:
        if self is TopPagesReportsResponseBucketingGranularityPeriod.DAY:
            return day()
