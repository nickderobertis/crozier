

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlayerUpdateMetadataArchitecture(enum.StrEnum):
    """
    Tilecast Edge only.
    """

    X8664 = "x86_64"
    AARCH64 = "aarch64"

    def visit(self, x8664: typing.Callable[[], T_Result], aarch64: typing.Callable[[], T_Result]) -> T_Result:
        if self is PlayerUpdateMetadataArchitecture.X8664:
            return x8664()
        if self is PlayerUpdateMetadataArchitecture.AARCH64:
            return aarch64()
