

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentCompression(enum.StrEnum):
    """
    Compression type for document store
    """

    NONE = "None"
    LZ4 = "Lz4"
    SNAPPY = "Snappy"
    ZSTD = "Zstd"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        lz4: typing.Callable[[], T_Result],
        snappy: typing.Callable[[], T_Result],
        zstd: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocumentCompression.NONE:
            return none()
        if self is DocumentCompression.LZ4:
            return lz4()
        if self is DocumentCompression.SNAPPY:
            return snappy()
        if self is DocumentCompression.ZSTD:
            return zstd()
