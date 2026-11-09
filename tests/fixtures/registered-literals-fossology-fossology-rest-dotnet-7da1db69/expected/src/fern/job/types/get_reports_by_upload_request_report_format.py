

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetReportsByUploadRequestReportFormat(enum.StrEnum):
    DEP5 = "dep5"
    SPDX2 = "spdx2"
    SPDX2TV = "spdx2tv"
    READMEOSS = "readmeoss"
    UNIFIEDREPORT = "unifiedreport"
    CLIXML = "clixml"
    CYCLONEDX = "cyclonedx"

    def visit(
        self,
        dep5: typing.Callable[[], T_Result],
        spdx2: typing.Callable[[], T_Result],
        spdx2tv: typing.Callable[[], T_Result],
        readmeoss: typing.Callable[[], T_Result],
        unifiedreport: typing.Callable[[], T_Result],
        clixml: typing.Callable[[], T_Result],
        cyclonedx: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetReportsByUploadRequestReportFormat.DEP5:
            return dep5()
        if self is GetReportsByUploadRequestReportFormat.SPDX2:
            return spdx2()
        if self is GetReportsByUploadRequestReportFormat.SPDX2TV:
            return spdx2tv()
        if self is GetReportsByUploadRequestReportFormat.READMEOSS:
            return readmeoss()
        if self is GetReportsByUploadRequestReportFormat.UNIFIEDREPORT:
            return unifiedreport()
        if self is GetReportsByUploadRequestReportFormat.CLIXML:
            return clixml()
        if self is GetReportsByUploadRequestReportFormat.CYCLONEDX:
            return cyclonedx()
