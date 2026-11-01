

import typing

EtcdKeyRotationStatusPhase = typing.Union[
    typing.Literal["prepare", "add_secondary", "promote_primary", "rewrite", "remove_old_keys", "finalize"], typing.Any
]
