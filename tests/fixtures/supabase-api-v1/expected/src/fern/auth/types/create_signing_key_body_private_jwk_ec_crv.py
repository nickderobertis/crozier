

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkEcCrv(enum.StrEnum):
    P256 = "P-256"

    def visit(self, p256: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkEcCrv.P256:
            return p256()
