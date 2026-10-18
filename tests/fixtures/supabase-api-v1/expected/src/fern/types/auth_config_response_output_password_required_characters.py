

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthConfigResponseOutputPasswordRequiredCharacters(enum.StrEnum):
    ABCDEFGHIJKLMNOPQRSTUVWXYZ_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:0123456789"
    )
    EMPTY = ""

    def visit(
        self,
        abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz0123456789: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is AuthConfigResponseOutputPasswordRequiredCharacters.ABCDEFGHIJKLMNOPQRSTUVWXYZ_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
        ):
            return abcdefghijklmnopqrstuvwxyz_abcdefghijklmnopqrstuvwxyz0123456789()
        if self is AuthConfigResponseOutputPasswordRequiredCharacters.EMPTY:
            return empty()
