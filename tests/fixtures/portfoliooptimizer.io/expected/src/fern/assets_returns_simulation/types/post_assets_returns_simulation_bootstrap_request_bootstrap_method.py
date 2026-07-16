

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod(str, enum.Enum):
    """
    The bootstrap method to use
    """

    IID = "iid"
    CIRCULAR_BLOCK = "circularBlock"
    STATIONARY_BLOCK = "stationaryBlock"

    def visit(
        self,
        iid: typing.Callable[[], T_Result],
        circular_block: typing.Callable[[], T_Result],
        stationary_block: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod.IID:
            return iid()
        if self is PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod.CIRCULAR_BLOCK:
            return circular_block()
        if self is PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod.STATIONARY_BLOCK:
            return stationary_block()
