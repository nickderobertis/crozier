

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyRiskScoreModelRuleType(enum.StrEnum):
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
        if self is PolicyRiskScoreModelRuleType.CONFIG:
            return config()
        if self is PolicyRiskScoreModelRuleType.NETWORK:
            return network()
        if self is PolicyRiskScoreModelRuleType.AUDIT_EVENT:
            return audit_event()
        if self is PolicyRiskScoreModelRuleType.DLP:
            return dlp()
        if self is PolicyRiskScoreModelRuleType.IAM:
            return iam()
        if self is PolicyRiskScoreModelRuleType.NETWORK_CONFIG:
            return network_config()
