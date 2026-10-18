

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkEcUse(enum.StrEnum):
    SIG = "sig"

    def visit(self, sig: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkEcUse.SIG:
            return sig()
