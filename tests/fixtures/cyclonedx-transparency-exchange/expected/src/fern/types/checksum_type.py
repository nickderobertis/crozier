

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChecksumType(enum.StrEnum):
    """
    Checksum algorithm
    """

    MD5 = "MD5"
    SHA1 = "SHA-1"
    SHA256 = "SHA-256"
    SHA384 = "SHA-384"
    SHA512 = "SHA-512"
    SHA3256 = "SHA3-256"
    SHA3384 = "SHA3-384"
    SHA3512 = "SHA3-512"
    BLAKE2B256 = "BLAKE2b-256"
    BLAKE2B384 = "BLAKE2b-384"
    BLAKE2B512 = "BLAKE2b-512"
    BLAKE3 = "BLAKE3"

    def visit(
        self,
        md5: typing.Callable[[], T_Result],
        sha1: typing.Callable[[], T_Result],
        sha256: typing.Callable[[], T_Result],
        sha384: typing.Callable[[], T_Result],
        sha512: typing.Callable[[], T_Result],
        sha3256: typing.Callable[[], T_Result],
        sha3384: typing.Callable[[], T_Result],
        sha3512: typing.Callable[[], T_Result],
        blake2b256: typing.Callable[[], T_Result],
        blake2b384: typing.Callable[[], T_Result],
        blake2b512: typing.Callable[[], T_Result],
        blake3: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChecksumType.MD5:
            return md5()
        if self is ChecksumType.SHA1:
            return sha1()
        if self is ChecksumType.SHA256:
            return sha256()
        if self is ChecksumType.SHA384:
            return sha384()
        if self is ChecksumType.SHA512:
            return sha512()
        if self is ChecksumType.SHA3256:
            return sha3256()
        if self is ChecksumType.SHA3384:
            return sha3384()
        if self is ChecksumType.SHA3512:
            return sha3512()
        if self is ChecksumType.BLAKE2B256:
            return blake2b256()
        if self is ChecksumType.BLAKE2B384:
            return blake2b384()
        if self is ChecksumType.BLAKE2B512:
            return blake2b512()
        if self is ChecksumType.BLAKE3:
            return blake3()
