

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkRsaAlg(enum.StrEnum):
    RS256 = "RS256"

    def visit(self, rs256: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkRsaAlg.RS256:
            return rs256()
