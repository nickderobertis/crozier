

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListSecretKeysCommandType(enum.StrEnum):
    LIST_SECRET_KEYS = "list-secret-keys"

    def visit(self, list_secret_keys: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListSecretKeysCommandType.LIST_SECRET_KEYS:
            return list_secret_keys()
