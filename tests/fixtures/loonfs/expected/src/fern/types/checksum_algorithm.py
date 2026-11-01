

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChecksumAlgorithm(enum.StrEnum):
    """
    A supported checksum algorithm.
    """

    CRC64NVME = "crc64nvme"
    CRC32C = "crc32c"

    def visit(self, crc64nvme: typing.Callable[[], T_Result], crc32c: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChecksumAlgorithm.CRC64NVME:
            return crc64nvme()
        if self is ChecksumAlgorithm.CRC32C:
            return crc32c()
