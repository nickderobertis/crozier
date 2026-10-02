

import typing

PolicyModelPolicyType = typing.Union[
    typing.Literal[
        "config",
        "network",
        "audit_event",
        "anomaly",
        "data",
        "iam",
        "workload_vulnerability",
        "workload_incident",
        "api",
        "attack_path",
        "malware",
        "grayware",
    ],
    typing.Any,
]
