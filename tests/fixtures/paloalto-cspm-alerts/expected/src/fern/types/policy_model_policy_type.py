

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PolicyModelPolicyType(enum.StrEnum):
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
        if self is PolicyModelPolicyType.CONFIG:
            return config()
        if self is PolicyModelPolicyType.NETWORK:
            return network()
        if self is PolicyModelPolicyType.AUDIT_EVENT:
            return audit_event()
        if self is PolicyModelPolicyType.ANOMALY:
            return anomaly()
        if self is PolicyModelPolicyType.DATA:
            return data()
        if self is PolicyModelPolicyType.IAM:
            return iam()
        if self is PolicyModelPolicyType.WORKLOAD_VULNERABILITY:
            return workload_vulnerability()
        if self is PolicyModelPolicyType.WORKLOAD_INCIDENT:
            return workload_incident()
        if self is PolicyModelPolicyType.API:
            return api()
        if self is PolicyModelPolicyType.ATTACK_PATH:
            return attack_path()
        if self is PolicyModelPolicyType.MALWARE:
            return malware()
        if self is PolicyModelPolicyType.GRAYWARE:
            return grayware()
