

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SslMode(enum.StrEnum):
    DISABLE = "disable"
    ALLOW = "allow"
    PREFER = "prefer"
    REQUIRE = "require"
    VERIFY_CA = "verify-ca"
    VERIFY_FULL = "verify-full"

    def visit(
        self,
        disable: typing.Callable[[], T_Result],
        allow: typing.Callable[[], T_Result],
        prefer: typing.Callable[[], T_Result],
        require: typing.Callable[[], T_Result],
        verify_ca: typing.Callable[[], T_Result],
        verify_full: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SslMode.DISABLE:
            return disable()
        if self is SslMode.ALLOW:
            return allow()
        if self is SslMode.PREFER:
            return prefer()
        if self is SslMode.REQUIRE:
            return require()
        if self is SslMode.VERIFY_CA:
            return verify_ca()
        if self is SslMode.VERIFY_FULL:
            return verify_full()
