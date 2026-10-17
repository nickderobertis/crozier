

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkOctAlg(enum.StrEnum):
    HS256 = "HS256"

    def visit(self, hs256: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkOctAlg.HS256:
            return hs256()
