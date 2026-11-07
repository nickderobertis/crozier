

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SignedBundleV2SignatureHashAlg(enum.StrEnum):
    SHA256 = "sha256"
    SHA384 = "sha384"

    def visit(self, sha256: typing.Callable[[], T_Result], sha384: typing.Callable[[], T_Result]) -> T_Result:
        if self is SignedBundleV2SignatureHashAlg.SHA256:
            return sha256()
        if self is SignedBundleV2SignatureHashAlg.SHA384:
            return sha384()
