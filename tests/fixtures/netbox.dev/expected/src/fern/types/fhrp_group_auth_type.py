

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FhrpGroupAuthType(enum.StrEnum):
    PLAINTEXT = "plaintext"
    MD5 = "md5"

    def visit(self, plaintext: typing.Callable[[], T_Result], md5: typing.Callable[[], T_Result]) -> T_Result:
        if self is FhrpGroupAuthType.PLAINTEXT:
            return plaintext()
        if self is FhrpGroupAuthType.MD5:
            return md5()
