

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class SignatureDigestVersionsRequestAlgorithm(enum.StrEnum):
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"

    def visit(
        self,
        sha1: typing.Callable[[], T_Result],
        sha256: typing.Callable[[], T_Result],
        sha384: typing.Callable[[], T_Result],
        sha512: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SignatureDigestVersionsRequestAlgorithm.SHA1:
            return sha1()
        if self is SignatureDigestVersionsRequestAlgorithm.SHA256:
            return sha256()
        if self is SignatureDigestVersionsRequestAlgorithm.SHA384:
            return sha384()
        if self is SignatureDigestVersionsRequestAlgorithm.SHA512:
            return sha512()
