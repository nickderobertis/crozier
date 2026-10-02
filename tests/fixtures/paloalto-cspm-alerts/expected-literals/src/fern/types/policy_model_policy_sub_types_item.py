

import typing

PolicyModelPolicySubTypesItem = typing.Union[
    typing.Literal[
        "run",
        "build",
        "run_and_build",
        "audit",
        "data_classification",
        "dns",
        "malware",
        "network_event",
        "network",
        "ueba",
        "permissions",
        "network_config",
        "identity",
        "sensitive_data_exposure",
        "internet_exposure",
        "injections",
        "vulnerability_scanning",
        "shellshock",
        "known_bots",
        "unknown_bots",
        "virtual_patches",
        "event",
        "misconfig_and_event",
        "misconfig",
        "host",
        "container_image",
    ],
    typing.Any,
]
