

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PricingPlanClassification(enum.StrEnum):
    TIER = "TIER"
    LICENSE = "LICENSE"

    def visit(self, tier: typing.Callable[[], T_Result], license: typing.Callable[[], T_Result]) -> T_Result:
        if self is PricingPlanClassification.TIER:
            return tier()
        if self is PricingPlanClassification.LICENSE:
            return license()
