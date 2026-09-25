

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyRiskScoreModelPolicyType(enum.StrEnum):
    """
    Policy type. Policy type **anomaly** is read-only.
    """

    CONFIG = "config"
    NETWORK = "network"
    AUDIT_EVENT = "audit_event"
    ANOMALY = "anomaly"
    DATA = "data"
    IAM = "iam"
    WORKLOAD_VULNERABILITY = "workload_vulnerability"
    WORKLOAD_INCIDENT = "workload_incident"
    API = "api"
    ATTACK_PATH = "attack_path"
    MALWARE = "malware"
    GRAYWARE = "grayware"

    def visit(
        self,
        config: typing.Callable[[], T_Result],
        network: typing.Callable[[], T_Result],
        audit_event: typing.Callable[[], T_Result],
        anomaly: typing.Callable[[], T_Result],
        data: typing.Callable[[], T_Result],
        iam: typing.Callable[[], T_Result],
        workload_vulnerability: typing.Callable[[], T_Result],
        workload_incident: typing.Callable[[], T_Result],
        api: typing.Callable[[], T_Result],
        attack_path: typing.Callable[[], T_Result],
        malware: typing.Callable[[], T_Result],
        grayware: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PolicyRiskScoreModelPolicyType.CONFIG:
            return config()
        if self is PolicyRiskScoreModelPolicyType.NETWORK:
            return network()
        if self is PolicyRiskScoreModelPolicyType.AUDIT_EVENT:
            return audit_event()
        if self is PolicyRiskScoreModelPolicyType.ANOMALY:
            return anomaly()
        if self is PolicyRiskScoreModelPolicyType.DATA:
            return data()
        if self is PolicyRiskScoreModelPolicyType.IAM:
            return iam()
        if self is PolicyRiskScoreModelPolicyType.WORKLOAD_VULNERABILITY:
            return workload_vulnerability()
        if self is PolicyRiskScoreModelPolicyType.WORKLOAD_INCIDENT:
            return workload_incident()
        if self is PolicyRiskScoreModelPolicyType.API:
            return api()
        if self is PolicyRiskScoreModelPolicyType.ATTACK_PATH:
            return attack_path()
        if self is PolicyRiskScoreModelPolicyType.MALWARE:
            return malware()
        if self is PolicyRiskScoreModelPolicyType.GRAYWARE:
            return grayware()
