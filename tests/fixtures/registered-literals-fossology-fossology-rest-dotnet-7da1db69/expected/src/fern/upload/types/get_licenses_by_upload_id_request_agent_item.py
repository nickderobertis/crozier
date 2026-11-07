

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetLicensesByUploadIdRequestAgentItem(enum.StrEnum):
    NOMOS = "nomos"
    MONK = "monk"
    NINKA = "ninka"
    OJO = "ojo"
    REPORT_IMPORT = "reportImport"
    RESO = "reso"
    SCANCODE = "scancode"

    def visit(
        self,
        nomos: typing.Callable[[], T_Result],
        monk: typing.Callable[[], T_Result],
        ninka: typing.Callable[[], T_Result],
        ojo: typing.Callable[[], T_Result],
        report_import: typing.Callable[[], T_Result],
        reso: typing.Callable[[], T_Result],
        scancode: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetLicensesByUploadIdRequestAgentItem.NOMOS:
            return nomos()
        if self is GetLicensesByUploadIdRequestAgentItem.MONK:
            return monk()
        if self is GetLicensesByUploadIdRequestAgentItem.NINKA:
            return ninka()
        if self is GetLicensesByUploadIdRequestAgentItem.OJO:
            return ojo()
        if self is GetLicensesByUploadIdRequestAgentItem.REPORT_IMPORT:
            return report_import()
        if self is GetLicensesByUploadIdRequestAgentItem.RESO:
            return reso()
        if self is GetLicensesByUploadIdRequestAgentItem.SCANCODE:
            return scancode()
