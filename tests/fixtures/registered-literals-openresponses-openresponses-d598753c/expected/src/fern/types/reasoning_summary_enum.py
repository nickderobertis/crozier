

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReasoningSummaryEnum(enum.StrEnum):
    CONCISE = "concise"
    DETAILED = "detailed"
    AUTO = "auto"

    def visit(
        self,
        concise: typing.Callable[[], T_Result],
        detailed: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReasoningSummaryEnum.CONCISE:
            return concise()
        if self is ReasoningSummaryEnum.DETAILED:
            return detailed()
        if self is ReasoningSummaryEnum.AUTO:
            return auto()
