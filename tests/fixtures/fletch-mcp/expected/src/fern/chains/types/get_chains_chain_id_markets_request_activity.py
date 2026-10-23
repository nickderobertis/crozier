

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdMarketsRequestActivity(enum.StrEnum):
    ALL = "all"
    TRADED = "traded"
    BUSY = "busy"
    QUIET = "quiet"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        traded: typing.Callable[[], T_Result],
        busy: typing.Callable[[], T_Result],
        quiet: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdMarketsRequestActivity.ALL:
            return all_()
        if self is GetChainsChainIdMarketsRequestActivity.TRADED:
            return traded()
        if self is GetChainsChainIdMarketsRequestActivity.BUSY:
            return busy()
        if self is GetChainsChainIdMarketsRequestActivity.QUIET:
            return quiet()
