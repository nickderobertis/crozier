

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchClientClientIdRequestRequestClientAuthMethodsItem(enum.StrEnum):
    PRIVATE_KEY_JWT = "private_key_jwt"

    def visit(self, private_key_jwt: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchClientClientIdRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT:
            return private_key_jwt()
