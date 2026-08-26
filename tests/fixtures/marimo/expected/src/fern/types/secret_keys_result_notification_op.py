

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SecretKeysResultNotificationOp(enum.StrEnum):
    SECRET_KEYS_RESULT = "secret-keys-result"

    def visit(self, secret_keys_result: typing.Callable[[], T_Result]) -> T_Result:
        if self is SecretKeysResultNotificationOp.SECRET_KEYS_RESULT:
            return secret_keys_result()
