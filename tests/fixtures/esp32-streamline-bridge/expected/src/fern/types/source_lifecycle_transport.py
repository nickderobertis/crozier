

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SourceLifecycleTransport(enum.StrEnum):
    CLEARTEXT = "cleartext"
    TLS_PSK = "tls-psk"

    def visit(self, cleartext: typing.Callable[[], T_Result], tls_psk: typing.Callable[[], T_Result]) -> T_Result:
        if self is SourceLifecycleTransport.CLEARTEXT:
            return cleartext()
        if self is SourceLifecycleTransport.TLS_PSK:
            return tls_psk()
