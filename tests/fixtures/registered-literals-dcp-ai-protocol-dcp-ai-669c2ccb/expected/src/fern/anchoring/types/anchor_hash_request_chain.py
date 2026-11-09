

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AnchorHashRequestChain(enum.StrEnum):
    BASE = "base"
    ARBITRUM = "arbitrum"
    OPTIMISM = "optimism"

    def visit(
        self,
        base: typing.Callable[[], T_Result],
        arbitrum: typing.Callable[[], T_Result],
        optimism: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AnchorHashRequestChain.BASE:
            return base()
        if self is AnchorHashRequestChain.ARBITRUM:
            return arbitrum()
        if self is AnchorHashRequestChain.OPTIMISM:
            return optimism()
