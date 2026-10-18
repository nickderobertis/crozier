

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkRsaUse(enum.StrEnum):
    SIG = "sig"

    def visit(self, sig: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkRsaUse.SIG:
            return sig()
