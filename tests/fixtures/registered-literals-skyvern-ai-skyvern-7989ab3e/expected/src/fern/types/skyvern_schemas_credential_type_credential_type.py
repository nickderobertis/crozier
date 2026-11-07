

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SkyvernSchemasCredentialTypeCredentialType(enum.StrEnum):
    SKYVERN = "skyvern"
    BITWARDEN = "bitwarden"
    ONE_PASSWORD = "1password"
    AZURE_VAULT = "azure_vault"

    def visit(
        self,
        skyvern: typing.Callable[[], T_Result],
        bitwarden: typing.Callable[[], T_Result],
        one_password: typing.Callable[[], T_Result],
        azure_vault: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SkyvernSchemasCredentialTypeCredentialType.SKYVERN:
            return skyvern()
        if self is SkyvernSchemasCredentialTypeCredentialType.BITWARDEN:
            return bitwarden()
        if self is SkyvernSchemasCredentialTypeCredentialType.ONE_PASSWORD:
            return one_password()
        if self is SkyvernSchemasCredentialTypeCredentialType.AZURE_VAULT:
            return azure_vault()
