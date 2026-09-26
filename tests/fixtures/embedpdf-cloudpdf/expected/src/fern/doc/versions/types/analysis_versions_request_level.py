

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class AnalysisVersionsRequestLevel(enum.StrEnum):
    NONE = "none"
    LTA = "lta"
    FILL = "fill"
    ANNOTATE = "annotate"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        lta: typing.Callable[[], T_Result],
        fill: typing.Callable[[], T_Result],
        annotate: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AnalysisVersionsRequestLevel.NONE:
            return none()
        if self is AnalysisVersionsRequestLevel.LTA:
            return lta()
        if self is AnalysisVersionsRequestLevel.FILL:
            return fill()
        if self is AnalysisVersionsRequestLevel.ANNOTATE:
            return annotate()
