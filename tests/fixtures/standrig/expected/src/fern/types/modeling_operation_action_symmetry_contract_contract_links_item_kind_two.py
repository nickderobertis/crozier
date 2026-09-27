

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionSymmetryContractContractLinksItemKindTwo(enum.StrEnum):
    WARP_PIN = "warp-pin"

    def visit(self, warp_pin: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionSymmetryContractContractLinksItemKindTwo.WARP_PIN:
            return warp_pin()
