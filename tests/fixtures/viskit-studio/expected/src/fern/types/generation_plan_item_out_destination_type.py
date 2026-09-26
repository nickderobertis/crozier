

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GenerationPlanItemOutDestinationType(enum.StrEnum):
    KIT_SLOT = "kit_slot"
    ASSET = "asset"

    def visit(self, kit_slot: typing.Callable[[], T_Result], asset: typing.Callable[[], T_Result]) -> T_Result:
        if self is GenerationPlanItemOutDestinationType.KIT_SLOT:
            return kit_slot()
        if self is GenerationPlanItemOutDestinationType.ASSET:
            return asset()
