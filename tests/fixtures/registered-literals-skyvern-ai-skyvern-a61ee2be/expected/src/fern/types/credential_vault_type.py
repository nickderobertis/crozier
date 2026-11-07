

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CredentialVaultType(enum.StrEnum):
    SKYVERN = "skyvern"
    BITWARDEN = "bitwarden"
    AZURE_VAULT = "azure_vault"
    GCP = "gcp"
    CUSTOM = "custom"

    def visit(
        self,
        skyvern: typing.Callable[[], T_Result],
        bitwarden: typing.Callable[[], T_Result],
        azure_vault: typing.Callable[[], T_Result],
        gcp: typing.Callable[[], T_Result],
        custom: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CredentialVaultType.SKYVERN:
            return skyvern()
        if self is CredentialVaultType.BITWARDEN:
            return bitwarden()
        if self is CredentialVaultType.AZURE_VAULT:
            return azure_vault()
        if self is CredentialVaultType.GCP:
            return gcp()
        if self is CredentialVaultType.CUSTOM:
            return custom()
