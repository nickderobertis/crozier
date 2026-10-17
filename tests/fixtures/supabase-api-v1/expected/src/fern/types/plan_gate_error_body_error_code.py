

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlanGateErrorBodyErrorCode(enum.StrEnum):
    """
    Machine-readable marker for plan-gated denials
    """

    ENTITLEMENT_REQUIRED = "entitlement_required"

    def visit(self, entitlement_required: typing.Callable[[], T_Result]) -> T_Result:
        if self is PlanGateErrorBodyErrorCode.ENTITLEMENT_REQUIRED:
            return entitlement_required()
