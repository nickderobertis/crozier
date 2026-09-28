

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindTwo(enum.StrEnum):
    WARP_PIN = "warp-pin"

    def visit(self, warp_pin: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionSymmetryArtmeshBindingsLinksItemKindTwo.WARP_PIN:
            return warp_pin()
