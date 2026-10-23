

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdMarketsRequestKind(enum.StrEnum):
    ALL = "all"
    LISTED = "listed"
    COMMUNITY = "community"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        listed: typing.Callable[[], T_Result],
        community: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdMarketsRequestKind.ALL:
            return all_()
        if self is GetChainsChainIdMarketsRequestKind.LISTED:
            return listed()
        if self is GetChainsChainIdMarketsRequestKind.COMMUNITY:
            return community()
