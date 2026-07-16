

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OrderServiceChargeCalculationPhase(str, enum.Enum):
    """
    Represents a phase in the process of calculating order totals.
    Service charges are applied after the indicated phase.

    [Read more about how order totals are calculated.](https://developer.squareup.com/docs/orders-api/how-it-works#how-totals-are-calculated)
    """

    SUBTOTAL_PHASE = "SUBTOTAL_PHASE"
    TOTAL_PHASE = "TOTAL_PHASE"

    def visit(
        self, subtotal_phase: typing.Callable[[], T_Result], total_phase: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is OrderServiceChargeCalculationPhase.SUBTOTAL_PHASE:
            return subtotal_phase()
        if self is OrderServiceChargeCalculationPhase.TOTAL_PHASE:
            return total_phase()
