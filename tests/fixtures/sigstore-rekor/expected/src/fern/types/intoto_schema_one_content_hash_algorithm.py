

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IntotoSchemaOneContentHashAlgorithm(enum.StrEnum):
    """
    The hashing function used to compute the hash value
    """

    SHA256 = "sha256"

    def visit(self, sha256: typing.Callable[[], T_Result]) -> T_Result:
        if self is IntotoSchemaOneContentHashAlgorithm.SHA256:
            return sha256()
