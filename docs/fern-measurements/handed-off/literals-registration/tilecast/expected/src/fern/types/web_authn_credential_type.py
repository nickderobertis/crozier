

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebAuthnCredentialType(enum.StrEnum):
    PUBLIC_KEY = "public-key"

    def visit(self, public_key: typing.Callable[[], T_Result]) -> T_Result:
        if self is WebAuthnCredentialType.PUBLIC_KEY:
            return public_key()
