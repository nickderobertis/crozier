

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TotphMacAlgo(enum.StrEnum):
    """
    Supported HMAC algorithms for Time-based one time passwords
    """

    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA512 = "sha512"

    def visit(
        self,
        sha1: typing.Callable[[], T_Result],
        sha256: typing.Callable[[], T_Result],
        sha512: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TotphMacAlgo.SHA1:
            return sha1()
        if self is TotphMacAlgo.SHA256:
            return sha256()
        if self is TotphMacAlgo.SHA512:
            return sha512()
