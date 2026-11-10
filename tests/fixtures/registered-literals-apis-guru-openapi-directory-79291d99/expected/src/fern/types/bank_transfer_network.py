

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BankTransferNetwork(enum.StrEnum):
    """
    The network or rails used for the transfer. Valid options are `ach`, `same-day-ach`, or `wire`.
    """

    ACH = "ach"
    SAME_DAY_ACH = "same-day-ach"
    WIRE = "wire"

    def visit(
        self,
        ach: typing.Callable[[], T_Result],
        same_day_ach: typing.Callable[[], T_Result],
        wire: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BankTransferNetwork.ACH:
            return ach()
        if self is BankTransferNetwork.SAME_DAY_ACH:
            return same_day_ach()
        if self is BankTransferNetwork.WIRE:
            return wire()
