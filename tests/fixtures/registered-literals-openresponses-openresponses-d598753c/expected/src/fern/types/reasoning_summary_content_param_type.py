

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReasoningSummaryContentParamType(enum.StrEnum):
    """
    The content type. Always `summary_text`.
    """

    SUMMARY_TEXT = "summary_text"

    def visit(self, summary_text: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReasoningSummaryContentParamType.SUMMARY_TEXT:
            return summary_text()
