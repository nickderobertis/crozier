

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetAlertsV2RequestPolicyType(enum.StrEnum):
    CONFIG = "config"
    NETWORK = "network"
    AUDIT_EVENT = "audit_event"

    def visit(
        self,
        config: typing.Callable[[], T_Result],
        network: typing.Callable[[], T_Result],
        audit_event: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetAlertsV2RequestPolicyType.CONFIG:
            return config()
        if self is GetAlertsV2RequestPolicyType.NETWORK:
            return network()
        if self is GetAlertsV2RequestPolicyType.AUDIT_EVENT:
            return audit_event()
