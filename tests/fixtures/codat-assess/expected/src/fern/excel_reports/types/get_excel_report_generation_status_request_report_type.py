

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetExcelReportGenerationStatusRequestReportType(enum.StrEnum):
    AUDIT = "audit"
    ENHANCED_FINANCIALS = "enhancedFinancials"

    def visit(
        self, audit: typing.Callable[[], T_Result], enhanced_financials: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GetExcelReportGenerationStatusRequestReportType.AUDIT:
            return audit()
        if self is GetExcelReportGenerationStatusRequestReportType.ENHANCED_FINANCIALS:
            return enhanced_financials()
