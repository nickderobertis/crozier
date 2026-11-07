

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NoiseMeterHistoryScreensRequestRange(enum.StrEnum):
    TODAY = "today"
    YESTERDAY = "yesterday"
    SEVEN_D = "7d"
    THIRTY_D = "30d"

    def visit(
        self,
        today: typing.Callable[[], T_Result],
        yesterday: typing.Callable[[], T_Result],
        seven_d: typing.Callable[[], T_Result],
        thirty_d: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NoiseMeterHistoryScreensRequestRange.TODAY:
            return today()
        if self is NoiseMeterHistoryScreensRequestRange.YESTERDAY:
            return yesterday()
        if self is NoiseMeterHistoryScreensRequestRange.SEVEN_D:
            return seven_d()
        if self is NoiseMeterHistoryScreensRequestRange.THIRTY_D:
            return thirty_d()
