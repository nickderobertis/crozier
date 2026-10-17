

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyAlgorithm(enum.StrEnum):
    ED_DSA = "EdDSA"
    ES256 = "ES256"
    RS256 = "RS256"
    HS256 = "HS256"

    def visit(
        self,
        ed_dsa: typing.Callable[[], T_Result],
        es256: typing.Callable[[], T_Result],
        rs256: typing.Callable[[], T_Result],
        hs256: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateSigningKeyBodyAlgorithm.ED_DSA:
            return ed_dsa()
        if self is CreateSigningKeyBodyAlgorithm.ES256:
            return es256()
        if self is CreateSigningKeyBodyAlgorithm.RS256:
            return rs256()
        if self is CreateSigningKeyBodyAlgorithm.HS256:
            return hs256()
