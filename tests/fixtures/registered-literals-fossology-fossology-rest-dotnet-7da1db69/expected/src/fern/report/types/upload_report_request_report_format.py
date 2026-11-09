

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UploadReportRequestReportFormat(enum.StrEnum):
    DECISIONIMPORTER = "decisionimporter"
    SPDXRDF = "spdxrdf"

    def visit(
        self, decisionimporter: typing.Callable[[], T_Result], spdxrdf: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is UploadReportRequestReportFormat.DECISIONIMPORTER:
            return decisionimporter()
        if self is UploadReportRequestReportFormat.SPDXRDF:
            return spdxrdf()
