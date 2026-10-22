

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransactionType(enum.StrEnum):
    RGB_SEND = "RgbSend"
    DRAIN = "Drain"
    CREATE_UTXOS = "CreateUtxos"
    SEND_BTC = "SendBtc"
    INCOMING = "Incoming"

    def visit(
        self,
        rgb_send: typing.Callable[[], T_Result],
        drain: typing.Callable[[], T_Result],
        create_utxos: typing.Callable[[], T_Result],
        send_btc: typing.Callable[[], T_Result],
        incoming: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransactionType.RGB_SEND:
            return rgb_send()
        if self is TransactionType.DRAIN:
            return drain()
        if self is TransactionType.CREATE_UTXOS:
            return create_utxos()
        if self is TransactionType.SEND_BTC:
            return send_btc()
        if self is TransactionType.INCOMING:
            return incoming()
