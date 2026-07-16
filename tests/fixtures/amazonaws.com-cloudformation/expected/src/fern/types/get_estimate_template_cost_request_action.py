

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetEstimateTemplateCostRequestAction(str, enum.Enum):
    ESTIMATE_TEMPLATE_COST = "EstimateTemplateCost"

    def visit(self, estimate_template_cost: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetEstimateTemplateCostRequestAction.ESTIMATE_TEMPLATE_COST:
            return estimate_template_cost()
