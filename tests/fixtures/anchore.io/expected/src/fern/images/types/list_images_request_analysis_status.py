

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListImagesRequestAnalysisStatus(enum.StrEnum):
    NOT_ANALYZED = "not_analyzed"
    ANALYZED = "analyzed"
    ANALYZING = "analyzing"
    ANALYSIS_FAILED = "analysis_failed"

    def visit(
        self,
        not_analyzed: typing.Callable[[], T_Result],
        analyzed: typing.Callable[[], T_Result],
        analyzing: typing.Callable[[], T_Result],
        analysis_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListImagesRequestAnalysisStatus.NOT_ANALYZED:
            return not_analyzed()
        if self is ListImagesRequestAnalysisStatus.ANALYZED:
            return analyzed()
        if self is ListImagesRequestAnalysisStatus.ANALYZING:
            return analyzing()
        if self is ListImagesRequestAnalysisStatus.ANALYSIS_FAILED:
            return analysis_failed()
