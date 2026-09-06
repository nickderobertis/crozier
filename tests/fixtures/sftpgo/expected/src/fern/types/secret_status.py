

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SecretStatus(enum.StrEnum):
    """
    Set to "Plain" to add or update an existing secret, set to "Redacted" to preserve the existing value
    """

    PLAIN = "Plain"
    AES256GCM = "AES-256-GCM"
    SECRETBOX = "Secretbox"
    GCP = "GCP"
    AWS = "AWS"
    VAULT_TRANSIT = "VaultTransit"
    AZURE_KEY_VAULT = "AzureKeyVault"
    REDACTED = "Redacted"

    def visit(
        self,
        plain: typing.Callable[[], T_Result],
        aes256gcm: typing.Callable[[], T_Result],
        secretbox: typing.Callable[[], T_Result],
        gcp: typing.Callable[[], T_Result],
        aws: typing.Callable[[], T_Result],
        vault_transit: typing.Callable[[], T_Result],
        azure_key_vault: typing.Callable[[], T_Result],
        redacted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SecretStatus.PLAIN:
            return plain()
        if self is SecretStatus.AES256GCM:
            return aes256gcm()
        if self is SecretStatus.SECRETBOX:
            return secretbox()
        if self is SecretStatus.GCP:
            return gcp()
        if self is SecretStatus.AWS:
            return aws()
        if self is SecretStatus.VAULT_TRANSIT:
            return vault_transit()
        if self is SecretStatus.AZURE_KEY_VAULT:
            return azure_key_vault()
        if self is SecretStatus.REDACTED:
            return redacted()
