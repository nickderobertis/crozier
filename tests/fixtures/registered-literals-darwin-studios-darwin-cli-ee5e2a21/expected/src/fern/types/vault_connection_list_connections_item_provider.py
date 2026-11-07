

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VaultConnectionListConnectionsItemProvider(enum.StrEnum):
    ONE_PASSWORD_SERVICE_ACCOUNT = "1password_service_account"
    ONE_PASSWORD_CONNECT = "1password_connect"
    OTHER = "other"

    def visit(
        self,
        one_password_service_account: typing.Callable[[], T_Result],
        one_password_connect: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VaultConnectionListConnectionsItemProvider.ONE_PASSWORD_SERVICE_ACCOUNT:
            return one_password_service_account()
        if self is VaultConnectionListConnectionsItemProvider.ONE_PASSWORD_CONNECT:
            return one_password_connect()
        if self is VaultConnectionListConnectionsItemProvider.OTHER:
            return other()
