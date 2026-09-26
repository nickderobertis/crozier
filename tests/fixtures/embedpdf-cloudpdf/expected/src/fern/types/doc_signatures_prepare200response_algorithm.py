

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocSignaturesPrepare200ResponseAlgorithm(enum.StrEnum):
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"

    def visit(
        self,
        sha256: typing.Callable[[], T_Result],
        sha384: typing.Callable[[], T_Result],
        sha512: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocSignaturesPrepare200ResponseAlgorithm.SHA256:
            return sha256()
        if self is DocSignaturesPrepare200ResponseAlgorithm.SHA384:
            return sha384()
        if self is DocSignaturesPrepare200ResponseAlgorithm.SHA512:
            return sha512()
