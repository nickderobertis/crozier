

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PlotRequestTide(enum.StrEnum):
    FLOOD = "flood"
    EBB = "ebb"
    SLACK = "slack"

    def visit(
        self,
        flood: typing.Callable[[], T_Result],
        ebb: typing.Callable[[], T_Result],
        slack: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlotRequestTide.FLOOD:
            return flood()
        if self is PlotRequestTide.EBB:
            return ebb()
        if self is PlotRequestTide.SLACK:
            return slack()
