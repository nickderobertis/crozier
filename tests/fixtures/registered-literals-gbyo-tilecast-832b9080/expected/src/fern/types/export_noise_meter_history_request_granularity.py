

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExportNoiseMeterHistoryRequestGranularity(enum.StrEnum):
    RAW = "raw"
    MINUTE = "minute"
    DAILY = "daily"

    def visit(
        self,
        raw: typing.Callable[[], T_Result],
        minute: typing.Callable[[], T_Result],
        daily: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExportNoiseMeterHistoryRequestGranularity.RAW:
            return raw()
        if self is ExportNoiseMeterHistoryRequestGranularity.MINUTE:
            return minute()
        if self is ExportNoiseMeterHistoryRequestGranularity.DAILY:
            return daily()
