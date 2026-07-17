

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaxCalculationPhase(enum.StrEnum):
    """
    When to calculate the taxes due on a cart.
    """

    TAX_SUBTOTAL_PHASE = "TAX_SUBTOTAL_PHASE"
    TAX_TOTAL_PHASE = "TAX_TOTAL_PHASE"

    def visit(
        self, tax_subtotal_phase: typing.Callable[[], T_Result], tax_total_phase: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TaxCalculationPhase.TAX_SUBTOTAL_PHASE:
            return tax_subtotal_phase()
        if self is TaxCalculationPhase.TAX_TOTAL_PHASE:
            return tax_total_phase()
