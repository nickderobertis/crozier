

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyPrivateJwkOkpAlg(enum.StrEnum):
    ED_DSA = "EdDSA"

    def visit(self, ed_dsa: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyPrivateJwkOkpAlg.ED_DSA:
            return ed_dsa()
