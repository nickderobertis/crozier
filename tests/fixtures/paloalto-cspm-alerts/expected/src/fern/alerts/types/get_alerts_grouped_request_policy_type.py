

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAlertsGroupedRequestPolicyType(enum.StrEnum):
    CONFIG = "config"
    NETWORK = "network"
    AUDIT_EVENT = "audit_event"

    def visit(
        self,
        config: typing.Callable[[], T_Result],
        network: typing.Callable[[], T_Result],
        audit_event: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAlertsGroupedRequestPolicyType.CONFIG:
            return config()
        if self is GetAlertsGroupedRequestPolicyType.NETWORK:
            return network()
        if self is GetAlertsGroupedRequestPolicyType.AUDIT_EVENT:
            return audit_event()
