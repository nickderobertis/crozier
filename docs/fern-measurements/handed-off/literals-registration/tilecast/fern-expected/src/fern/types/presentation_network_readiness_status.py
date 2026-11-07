

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PresentationNetworkReadinessStatus(enum.StrEnum):
    NOT_APPLICABLE = "not_applicable"
    NETWORK_MANAGER_UNAVAILABLE = "network_manager_unavailable"
    HELPER_MISSING = "helper_missing"
    HELPER_UNHEALTHY = "helper_unhealthy"
    UNSUPPORTED = "unsupported"
    WIFI_ADAPTER_UNAVAILABLE = "wifi_adapter_unavailable"
    UNASSIGNED = "unassigned"
    REPORTING_PENDING = "reporting_pending"
    CONNECTED = "connected"
    FAILED = "failed"
    CONFIGURATION_PENDING = "configuration_pending"
    READY = "ready"

    def visit(
        self,
        not_applicable: typing.Callable[[], T_Result],
        network_manager_unavailable: typing.Callable[[], T_Result],
        helper_missing: typing.Callable[[], T_Result],
        helper_unhealthy: typing.Callable[[], T_Result],
        unsupported: typing.Callable[[], T_Result],
        wifi_adapter_unavailable: typing.Callable[[], T_Result],
        unassigned: typing.Callable[[], T_Result],
        reporting_pending: typing.Callable[[], T_Result],
        connected: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        configuration_pending: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PresentationNetworkReadinessStatus.NOT_APPLICABLE:
            return not_applicable()
        if self is PresentationNetworkReadinessStatus.NETWORK_MANAGER_UNAVAILABLE:
            return network_manager_unavailable()
        if self is PresentationNetworkReadinessStatus.HELPER_MISSING:
            return helper_missing()
        if self is PresentationNetworkReadinessStatus.HELPER_UNHEALTHY:
            return helper_unhealthy()
        if self is PresentationNetworkReadinessStatus.UNSUPPORTED:
            return unsupported()
        if self is PresentationNetworkReadinessStatus.WIFI_ADAPTER_UNAVAILABLE:
            return wifi_adapter_unavailable()
        if self is PresentationNetworkReadinessStatus.UNASSIGNED:
            return unassigned()
        if self is PresentationNetworkReadinessStatus.REPORTING_PENDING:
            return reporting_pending()
        if self is PresentationNetworkReadinessStatus.CONNECTED:
            return connected()
        if self is PresentationNetworkReadinessStatus.FAILED:
            return failed()
        if self is PresentationNetworkReadinessStatus.CONFIGURATION_PENDING:
            return configuration_pending()
        if self is PresentationNetworkReadinessStatus.READY:
            return ready()
