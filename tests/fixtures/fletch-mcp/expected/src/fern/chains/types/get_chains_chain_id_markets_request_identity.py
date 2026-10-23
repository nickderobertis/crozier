

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdMarketsRequestIdentity(enum.StrEnum):
    ALL = "all"
    DOMINANT = "dominant"
    SAME_NAME = "same_name"
    CLOSE_CALL = "close_call"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        dominant: typing.Callable[[], T_Result],
        same_name: typing.Callable[[], T_Result],
        close_call: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetChainsChainIdMarketsRequestIdentity.ALL:
            return all_()
        if self is GetChainsChainIdMarketsRequestIdentity.DOMINANT:
            return dominant()
        if self is GetChainsChainIdMarketsRequestIdentity.SAME_NAME:
            return same_name()
        if self is GetChainsChainIdMarketsRequestIdentity.CLOSE_CALL:
            return close_call()
