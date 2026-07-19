

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HashedrekordSchemaDataHashAlgorithm(enum.StrEnum):
    """
    The hashing function used to compute the hash value
    """

    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"

    def visit(
        self,
        sha256: typing.Callable[[], T_Result],
        sha384: typing.Callable[[], T_Result],
        sha512: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is HashedrekordSchemaDataHashAlgorithm.SHA256:
            return sha256()
        if self is HashedrekordSchemaDataHashAlgorithm.SHA384:
            return sha384()
        if self is HashedrekordSchemaDataHashAlgorithm.SHA512:
            return sha512()
