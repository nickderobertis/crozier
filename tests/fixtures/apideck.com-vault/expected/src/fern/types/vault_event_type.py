

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class VaultEventType(str, enum.Enum):
    ALL = "*"
    VAULT_CONNECTION_CREATED = "vault.connection.created"
    VAULT_CONNECTION_UPDATED = "vault.connection.updated"
    VAULT_CONNECTION_DISABLED = "vault.connection.disabled"
    VAULT_CONNECTION_DELETED = "vault.connection.deleted"
    VAULT_CONNECTION_CALLABLE = "vault.connection.callable"
    VAULT_CONNECTION_TOKEN_REFRESH_FAILED = "vault.connection.token_refresh.failed"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        vault_connection_created: typing.Callable[[], T_Result],
        vault_connection_updated: typing.Callable[[], T_Result],
        vault_connection_disabled: typing.Callable[[], T_Result],
        vault_connection_deleted: typing.Callable[[], T_Result],
        vault_connection_callable: typing.Callable[[], T_Result],
        vault_connection_token_refresh_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VaultEventType.ALL:
            return all_()
        if self is VaultEventType.VAULT_CONNECTION_CREATED:
            return vault_connection_created()
        if self is VaultEventType.VAULT_CONNECTION_UPDATED:
            return vault_connection_updated()
        if self is VaultEventType.VAULT_CONNECTION_DISABLED:
            return vault_connection_disabled()
        if self is VaultEventType.VAULT_CONNECTION_DELETED:
            return vault_connection_deleted()
        if self is VaultEventType.VAULT_CONNECTION_CALLABLE:
            return vault_connection_callable()
        if self is VaultEventType.VAULT_CONNECTION_TOKEN_REFRESH_FAILED:
            return vault_connection_token_refresh_failed()
