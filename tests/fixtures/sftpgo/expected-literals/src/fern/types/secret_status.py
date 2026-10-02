

import typing

SecretStatus = typing.Union[
    typing.Literal["Plain", "AES-256-GCM", "Secretbox", "GCP", "AWS", "VaultTransit", "AzureKeyVault", "Redacted"],
    typing.Any,
]
