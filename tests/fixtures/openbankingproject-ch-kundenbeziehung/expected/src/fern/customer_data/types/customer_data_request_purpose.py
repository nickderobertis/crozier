

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CustomerDataRequestPurpose(enum.StrEnum):
    KUNDENBEZIEHUNGSEROFFNUNG = "kundenbeziehungseroffnung"
    RE_IDENTIFICATION = "re_identification"
    COMPLIANCE_UPDATE = "compliance_update"

    def visit(
        self,
        kundenbeziehungseroffnung: typing.Callable[[], T_Result],
        re_identification: typing.Callable[[], T_Result],
        compliance_update: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomerDataRequestPurpose.KUNDENBEZIEHUNGSEROFFNUNG:
            return kundenbeziehungseroffnung()
        if self is CustomerDataRequestPurpose.RE_IDENTIFICATION:
            return re_identification()
        if self is CustomerDataRequestPurpose.COMPLIANCE_UPDATE:
            return compliance_update()
