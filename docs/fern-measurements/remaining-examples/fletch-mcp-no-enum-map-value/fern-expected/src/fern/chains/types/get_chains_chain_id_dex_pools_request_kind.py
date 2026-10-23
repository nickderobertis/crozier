

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdDexPoolsRequestKind(enum.StrEnum):
    ALL = "all"
    LISTED = "listed"
    COMMUNITY = "community"
    LOOKALIKE = "lookalike"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        listed: typing.Callable[[], T_Result],
        community: typing.Callable[[], T_Result],
        lookalike: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdDexPoolsRequestKind.ALL:
            return all_()
        if self is GetChainsChainIdDexPoolsRequestKind.LISTED:
            return listed()
        if self is GetChainsChainIdDexPoolsRequestKind.COMMUNITY:
            return community()
        if self is GetChainsChainIdDexPoolsRequestKind.LOOKALIKE:
            return lookalike()
