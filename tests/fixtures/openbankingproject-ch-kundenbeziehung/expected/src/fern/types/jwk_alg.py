

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JwkAlg(enum.StrEnum):
    """
    Algorithm
    """

    PS256 = "PS256"
    ES256 = "ES256"
    ED_DSA = "EdDSA"

    def visit(
        self,
        ps256: typing.Callable[[], T_Result],
        es256: typing.Callable[[], T_Result],
        ed_dsa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is JwkAlg.PS256:
            return ps256()
        if self is JwkAlg.ES256:
            return es256()
        if self is JwkAlg.ED_DSA:
            return ed_dsa()
