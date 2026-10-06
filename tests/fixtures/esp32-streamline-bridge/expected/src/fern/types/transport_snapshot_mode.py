

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransportSnapshotMode(enum.StrEnum):
    CLEARTEXT = "cleartext"
    TLS_PSK = "tls-psk"

    def visit(self, cleartext: typing.Callable[[], T_Result], tls_psk: typing.Callable[[], T_Result]) -> T_Result:
        if self is TransportSnapshotMode.CLEARTEXT:
            return cleartext()
        if self is TransportSnapshotMode.TLS_PSK:
            return tls_psk()
