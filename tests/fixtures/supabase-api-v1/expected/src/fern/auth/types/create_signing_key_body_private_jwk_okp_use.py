

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkOkpUse(enum.StrEnum):
    SIG = "sig"

    def visit(self, sig: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkOkpUse.SIG:
            return sig()
