

import typing

UpdateInProgressType = typing.Union[
    typing.Literal[
        "etcd_encryption",
        "etcd_key_rotation",
        "k8s_upgrade",
        "cp_nodes_recycling",
        "oidc_enable",
        "spire_server_update",
        "certificate_renewal",
    ],
    typing.Any,
]
