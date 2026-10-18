

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkOkpCrv(enum.StrEnum):
    ED25519 = "Ed25519"

    def visit(self, ed25519: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkOkpCrv.ED25519:
            return ed25519()
