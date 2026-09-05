

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IkeCryptoProfilesHashItem(enum.StrEnum):
    """
    Hashing algorithm
    """

    MD5 = "md5"
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"

    def visit(
        self,
        md5: typing.Callable[[], T_Result],
        sha1: typing.Callable[[], T_Result],
        sha256: typing.Callable[[], T_Result],
        sha384: typing.Callable[[], T_Result],
        sha512: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IkeCryptoProfilesHashItem.MD5:
            return md5()
        if self is IkeCryptoProfilesHashItem.SHA1:
            return sha1()
        if self is IkeCryptoProfilesHashItem.SHA256:
            return sha256()
        if self is IkeCryptoProfilesHashItem.SHA384:
            return sha384()
        if self is IkeCryptoProfilesHashItem.SHA512:
            return sha512()
