

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateResponseBodyReasoningSummary(enum.StrEnum):
    """
    Controls whether the response includes a reasoning summary.
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
        if self is CreateResponseBodyReasoningSummary.CONCISE:
            return concise()
        if self is CreateResponseBodyReasoningSummary.DETAILED:
            return detailed()
        if self is CreateResponseBodyReasoningSummary.AUTO:
            return auto()
