

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BinMaterial(enum.StrEnum):
    GLASS = "glass"
    PAPER = "paper"
    METAL = "metal"

    def visit(
        self,
        glass: typing.Callable[[], T_Result],
        paper: typing.Callable[[], T_Result],
        metal: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BinMaterial.GLASS:
            return glass()
        if self is BinMaterial.PAPER:
            return paper()
        if self is BinMaterial.METAL:
            return metal()
