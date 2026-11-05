

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManifestScheduleType(enum.StrEnum):
    WEEKLY = "weekly"
    ONE_TIME = "one_time"

    def visit(self, weekly: typing.Callable[[], T_Result], one_time: typing.Callable[[], T_Result]) -> T_Result:
        if self is ManifestScheduleType.WEEKLY:
            return weekly()
        if self is ManifestScheduleType.ONE_TIME:
            return one_time()
