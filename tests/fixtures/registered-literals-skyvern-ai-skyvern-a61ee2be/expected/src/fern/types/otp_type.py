

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OtpType(enum.StrEnum):
    TOTP = "totp"
    MAGIC_LINK = "magic_link"

    def visit(self, totp: typing.Callable[[], T_Result], magic_link: typing.Callable[[], T_Result]) -> T_Result:
        if self is OtpType.TOTP:
            return totp()
        if self is OtpType.MAGIC_LINK:
            return magic_link()
