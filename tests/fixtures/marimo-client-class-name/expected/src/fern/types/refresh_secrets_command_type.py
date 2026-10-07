

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RefreshSecretsCommandType(enum.StrEnum):
    REFRESH_SECRETS = "refresh-secrets"

    def visit(self, refresh_secrets: typing.Callable[[], T_Result]) -> T_Result:
        if self is RefreshSecretsCommandType.REFRESH_SECRETS:
            return refresh_secrets()
