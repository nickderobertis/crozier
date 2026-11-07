

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SiacoinOriginSource(enum.StrEnum):
    """
    The source type of the siacoin output.
    """

    TRANSACTION = "transaction"
    MINER_PAYOUT = "minerPayout"
    CONTRACT_PAYOUT = "contractPayout"
    SIAFUND_CLAIM = "siafundClaim"
    FOUNDATION_SUBSIDY = "foundationSubsidy"
    UNKNOWN = "unknown"

    def visit(
        self,
        transaction: typing.Callable[[], T_Result],
        miner_payout: typing.Callable[[], T_Result],
        contract_payout: typing.Callable[[], T_Result],
        siafund_claim: typing.Callable[[], T_Result],
        foundation_subsidy: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SiacoinOriginSource.TRANSACTION:
            return transaction()
        if self is SiacoinOriginSource.MINER_PAYOUT:
            return miner_payout()
        if self is SiacoinOriginSource.CONTRACT_PAYOUT:
            return contract_payout()
        if self is SiacoinOriginSource.SIAFUND_CLAIM:
            return siafund_claim()
        if self is SiacoinOriginSource.FOUNDATION_SUBSIDY:
            return foundation_subsidy()
        if self is SiacoinOriginSource.UNKNOWN:
            return unknown()
