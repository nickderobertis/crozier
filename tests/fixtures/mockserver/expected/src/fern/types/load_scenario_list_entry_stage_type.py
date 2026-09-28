

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadScenarioListEntryStageType(enum.StrEnum):
    VU = "VU"
    RATE = "RATE"
    PAUSE = "PAUSE"

    def visit(
        self,
        vu: typing.Callable[[], T_Result],
        rate: typing.Callable[[], T_Result],
        pause: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadScenarioListEntryStageType.VU:
            return vu()
        if self is LoadScenarioListEntryStageType.RATE:
            return rate()
        if self is LoadScenarioListEntryStageType.PAUSE:
            return pause()
