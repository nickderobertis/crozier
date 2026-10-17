

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkRsaE(enum.StrEnum):
    AQAB = "AQAB"

    def visit(self, aqab: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkRsaE.AQAB:
            return aqab()
