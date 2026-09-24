

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReportGenerationConfigApiModelType(enum.StrEnum):
    """
    Report type. Default is COMPLIANCE.
    """

    COMPLIANCE = "COMPLIANCE"
    RIS = "RIS"
    INVENTORY_OVERVIEW = "INVENTORY_OVERVIEW"
    INVENTORY_DETAIL = "INVENTORY_DETAIL"

    def visit(
        self,
        compliance: typing.Callable[[], T_Result],
        ris: typing.Callable[[], T_Result],
        inventory_overview: typing.Callable[[], T_Result],
        inventory_detail: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReportGenerationConfigApiModelType.COMPLIANCE:
            return compliance()
        if self is ReportGenerationConfigApiModelType.RIS:
            return ris()
        if self is ReportGenerationConfigApiModelType.INVENTORY_OVERVIEW:
            return inventory_overview()
        if self is ReportGenerationConfigApiModelType.INVENTORY_DETAIL:
            return inventory_detail()
