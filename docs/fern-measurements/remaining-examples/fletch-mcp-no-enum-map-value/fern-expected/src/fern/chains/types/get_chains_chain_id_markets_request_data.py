

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdMarketsRequestData(enum.StrEnum):
    ALL = "all"
    PRICED = "priced"
    VOLUME = "volume"
    COMPLETE = "complete"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        priced: typing.Callable[[], T_Result],
        volume: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdMarketsRequestData.ALL:
            return all_()
        if self is GetChainsChainIdMarketsRequestData.PRICED:
            return priced()
        if self is GetChainsChainIdMarketsRequestData.VOLUME:
            return volume()
        if self is GetChainsChainIdMarketsRequestData.COMPLETE:
            return complete()
