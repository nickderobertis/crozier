

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkEcAlg(enum.StrEnum):
    ES256 = "ES256"

    def visit(self, es256: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkEcAlg.ES256:
            return es256()
