

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferKind(enum.StrEnum):
    ISSUANCE = "Issuance"
    RECEIVE_BLIND = "ReceiveBlind"
    RECEIVE_WITNESS = "ReceiveWitness"
    SEND = "Send"
    INFLATION = "Inflation"
    BURN = "Burn"

    def visit(
        self,
        issuance: typing.Callable[[], T_Result],
        receive_blind: typing.Callable[[], T_Result],
        receive_witness: typing.Callable[[], T_Result],
        send: typing.Callable[[], T_Result],
        inflation: typing.Callable[[], T_Result],
        burn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferKind.ISSUANCE:
            return issuance()
        if self is TransferKind.RECEIVE_BLIND:
            return receive_blind()
        if self is TransferKind.RECEIVE_WITNESS:
            return receive_witness()
        if self is TransferKind.SEND:
            return send()
        if self is TransferKind.INFLATION:
            return inflation()
        if self is TransferKind.BURN:
            return burn()
