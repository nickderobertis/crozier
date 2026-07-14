

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AnchoreImageAnalysisStatus(str, enum.Enum):
    """
    A state value for the current status of the analysis progress of the image
    """

    NOT_ANALYZED = "not_analyzed"
    ANALYZING = "analyzing"
    ANALYZED = "analyzed"
    ANALYSIS_FAILED = "analysis_failed"

    def visit(
        self,
        not_analyzed: typing.Callable[[], T_Result],
        analyzing: typing.Callable[[], T_Result],
        analyzed: typing.Callable[[], T_Result],
        analysis_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AnchoreImageAnalysisStatus.NOT_ANALYZED:
            return not_analyzed()
        if self is AnchoreImageAnalysisStatus.ANALYZING:
            return analyzing()
        if self is AnchoreImageAnalysisStatus.ANALYZED:
            return analyzed()
        if self is AnchoreImageAnalysisStatus.ANALYSIS_FAILED:
            return analysis_failed()
