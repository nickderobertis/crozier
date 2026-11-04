

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PresentationNetworkReadinessReportedState(enum.StrEnum):
    UNSUPPORTED = "unsupported"
    UNASSIGNED = "unassigned"
    PENDING = "pending"
    PROVISIONED = "provisioned"
    JOINING = "joining"
    CONNECTED = "connected"
    FAILED = "failed"

    def visit(
        self,
        unsupported: typing.Callable[[], T_Result],
        unassigned: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        provisioned: typing.Callable[[], T_Result],
        joining: typing.Callable[[], T_Result],
        connected: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PresentationNetworkReadinessReportedState.UNSUPPORTED:
            return unsupported()
        if self is PresentationNetworkReadinessReportedState.UNASSIGNED:
            return unassigned()
        if self is PresentationNetworkReadinessReportedState.PENDING:
            return pending()
        if self is PresentationNetworkReadinessReportedState.PROVISIONED:
            return provisioned()
        if self is PresentationNetworkReadinessReportedState.JOINING:
            return joining()
        if self is PresentationNetworkReadinessReportedState.CONNECTED:
            return connected()
        if self is PresentationNetworkReadinessReportedState.FAILED:
            return failed()
