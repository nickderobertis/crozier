

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseInProgressStreamingEventResponseReasoningSummary(enum.StrEnum):
    """
    A model-generated summary of its reasoning that was produced, if available.
    """

    CONCISE = "concise"
    DETAILED = "detailed"
    AUTO = "auto"

    def visit(
        self,
        concise: typing.Callable[[], T_Result],
        detailed: typing.Callable[[], T_Result],
        auto: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResponseInProgressStreamingEventResponseReasoningSummary.CONCISE:
            return concise()
        if self is ResponseInProgressStreamingEventResponseReasoningSummary.DETAILED:
            return detailed()
        if self is ResponseInProgressStreamingEventResponseReasoningSummary.AUTO:
            return auto()
