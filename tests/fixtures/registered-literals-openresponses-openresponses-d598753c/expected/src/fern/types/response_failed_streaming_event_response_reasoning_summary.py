

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResponseFailedStreamingEventResponseReasoningSummary(enum.StrEnum):
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
        if self is ResponseFailedStreamingEventResponseReasoningSummary.CONCISE:
            return concise()
        if self is ResponseFailedStreamingEventResponseReasoningSummary.DETAILED:
            return detailed()
        if self is ResponseFailedStreamingEventResponseReasoningSummary.AUTO:
            return auto()
