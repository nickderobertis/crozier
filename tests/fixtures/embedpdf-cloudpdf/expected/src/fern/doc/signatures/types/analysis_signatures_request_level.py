

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class AnalysisSignaturesRequestLevel(enum.StrEnum):
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
        if self is AnalysisSignaturesRequestLevel.NONE:
            return none()
        if self is AnalysisSignaturesRequestLevel.LTA:
            return lta()
        if self is AnalysisSignaturesRequestLevel.FILL:
            return fill()
        if self is AnalysisSignaturesRequestLevel.ANNOTATE:
            return annotate()
