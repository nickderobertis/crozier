

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyModelRuleType(enum.StrEnum):
    """
    Type of rule or RQL query
    """

    CONFIG = "Config"
    NETWORK = "Network"
    AUDIT_EVENT = "AuditEvent"
    DLP = "DLP"
    IAM = "IAM"
    NETWORK_CONFIG = "NetworkConfig"

    def visit(
        self,
        config: typing.Callable[[], T_Result],
        network: typing.Callable[[], T_Result],
        audit_event: typing.Callable[[], T_Result],
        dlp: typing.Callable[[], T_Result],
        iam: typing.Callable[[], T_Result],
        network_config: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PolicyModelRuleType.CONFIG:
            return config()
        if self is PolicyModelRuleType.NETWORK:
            return network()
        if self is PolicyModelRuleType.AUDIT_EVENT:
            return audit_event()
        if self is PolicyModelRuleType.DLP:
            return dlp()
        if self is PolicyModelRuleType.IAM:
            return iam()
        if self is PolicyModelRuleType.NETWORK_CONFIG:
            return network_config()
