

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EventType(enum.StrEnum):
    """
    The type of the event
    """

    MINER = "miner"
    FOUNDATION = "foundation"
    SIAFUND_CLAIM = "siafundClaim"
    V1TRANSACTION = "v1Transaction"
    V1CONTRACT_RESOLUTION = "v1ContractResolution"
    V2TRANSACTION = "v2Transaction"
    V2CONTRACT_RESOLUTION = "v2ContractResolution"

    def visit(
        self,
        miner: typing.Callable[[], T_Result],
        foundation: typing.Callable[[], T_Result],
        siafund_claim: typing.Callable[[], T_Result],
        v1transaction: typing.Callable[[], T_Result],
        v1contract_resolution: typing.Callable[[], T_Result],
        v2transaction: typing.Callable[[], T_Result],
        v2contract_resolution: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EventType.MINER:
            return miner()
        if self is EventType.FOUNDATION:
            return foundation()
        if self is EventType.SIAFUND_CLAIM:
            return siafund_claim()
        if self is EventType.V1TRANSACTION:
            return v1transaction()
        if self is EventType.V1CONTRACT_RESOLUTION:
            return v1contract_resolution()
        if self is EventType.V2TRANSACTION:
            return v2transaction()
        if self is EventType.V2CONTRACT_RESOLUTION:
            return v2contract_resolution()
