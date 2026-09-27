

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GenerateExcelReportRequestReportType(enum.StrEnum):
    AUDIT = "audit"
    ENHANCED_FINANCIALS = "enhancedFinancials"

    def visit(
        self, audit: typing.Callable[[], T_Result], enhanced_financials: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is GenerateExcelReportRequestReportType.AUDIT:
            return audit()
        if self is GenerateExcelReportRequestReportType.ENHANCED_FINANCIALS:
            return enhanced_financials()
