

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SignedBundleV1SignatureAlg(enum.StrEnum):
    ED25519 = "ed25519"

    def visit(self, ed25519: typing.Callable[[], T_Result]) -> T_Result:
        if self is SignedBundleV1SignatureAlg.ED25519:
            return ed25519()
