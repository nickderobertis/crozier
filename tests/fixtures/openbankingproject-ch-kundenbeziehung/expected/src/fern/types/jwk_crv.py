

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JwkCrv(enum.StrEnum):
    """
    Elliptic curve
    """

    P256 = "P-256"
    ED25519 = "Ed25519"

    def visit(self, p256: typing.Callable[[], T_Result], ed25519: typing.Callable[[], T_Result]) -> T_Result:
        if self is JwkCrv.P256:
            return p256()
        if self is JwkCrv.ED25519:
            return ed25519()
