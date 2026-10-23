

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetChainsChainIdStatusResponseSwapIndexerMode(enum.StrEnum):
    LIVE_AND_BACKWARDS = "live_and_backwards"

    def visit(self, live_and_backwards: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetChainsChainIdStatusResponseSwapIndexerMode.LIVE_AND_BACKWARDS:
            return live_and_backwards()
