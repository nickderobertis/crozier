

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SummarizationRequestBodySummarizationSummaryType(enum.StrEnum):
    """
    Type of summary. Bullets returns short bullet point style summaries, paragraph is generally more verbose and detailed.
    """

    PARAGRAPH = "paragraph"
    BULLETS = "bullets"

    def visit(self, paragraph: typing.Callable[[], T_Result], bullets: typing.Callable[[], T_Result]) -> T_Result:
        if self is SummarizationRequestBodySummarizationSummaryType.PARAGRAPH:
            return paragraph()
        if self is SummarizationRequestBodySummarizationSummaryType.BULLETS:
            return bullets()
