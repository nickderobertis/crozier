

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListReportsRequestReportView(enum.StrEnum):
    COMPLIANCE = "COMPLIANCE"
    RIS = "RIS"
    INVENTORY_DETAIL = "INVENTORY_DETAIL"
    INVENTORY_OVERVIEW = "INVENTORY_OVERVIEW"

    def visit(
        self,
        compliance: typing.Callable[[], T_Result],
        ris: typing.Callable[[], T_Result],
        inventory_detail: typing.Callable[[], T_Result],
        inventory_overview: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListReportsRequestReportView.COMPLIANCE:
            return compliance()
        if self is ListReportsRequestReportView.RIS:
            return ris()
        if self is ListReportsRequestReportView.INVENTORY_DETAIL:
            return inventory_detail()
        if self is ListReportsRequestReportView.INVENTORY_OVERVIEW:
            return inventory_overview()
