

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HashAlgorithm(enum.StrEnum):
    BLAKE3 = "blake3"

    def visit(self, blake3: typing.Callable[[], T_Result]) -> T_Result:
        if self is HashAlgorithm.BLAKE3:
            return blake3()
