

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VaultItemListItemsItemKind(enum.StrEnum):
    OAUTH_TOKEN = "oauth_token"
    API_KEY = "api_key"
    CLIENT_CREDENTIALS = "client_credentials"
    PASSWORD = "password"
    TOTP_SEED = "totp_seed"
    SSH_PRIVATE_KEY = "ssh_private_key"
    CERTIFICATE = "certificate"
    PROVIDER_SECRET = "provider_secret"

    def visit(
        self,
        oauth_token: typing.Callable[[], T_Result],
        api_key: typing.Callable[[], T_Result],
        client_credentials: typing.Callable[[], T_Result],
        password: typing.Callable[[], T_Result],
        totp_seed: typing.Callable[[], T_Result],
        ssh_private_key: typing.Callable[[], T_Result],
        certificate: typing.Callable[[], T_Result],
        provider_secret: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VaultItemListItemsItemKind.OAUTH_TOKEN:
            return oauth_token()
        if self is VaultItemListItemsItemKind.API_KEY:
            return api_key()
        if self is VaultItemListItemsItemKind.CLIENT_CREDENTIALS:
            return client_credentials()
        if self is VaultItemListItemsItemKind.PASSWORD:
            return password()
        if self is VaultItemListItemsItemKind.TOTP_SEED:
            return totp_seed()
        if self is VaultItemListItemsItemKind.SSH_PRIVATE_KEY:
            return ssh_private_key()
        if self is VaultItemListItemsItemKind.CERTIFICATE:
            return certificate()
        if self is VaultItemListItemsItemKind.PROVIDER_SECRET:
            return provider_secret()
