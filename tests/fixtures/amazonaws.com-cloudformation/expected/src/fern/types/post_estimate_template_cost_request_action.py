

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostEstimateTemplateCostRequestAction(enum.StrEnum):
    ESTIMATE_TEMPLATE_COST = "EstimateTemplateCost"

    def visit(self, estimate_template_cost: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostEstimateTemplateCostRequestAction.ESTIMATE_TEMPLATE_COST:
            return estimate_template_cost()
