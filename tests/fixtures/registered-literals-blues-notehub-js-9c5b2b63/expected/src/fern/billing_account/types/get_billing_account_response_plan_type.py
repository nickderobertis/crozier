

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetBillingAccountResponsePlanType(enum.StrEnum):
    ENTERPRISE = "Enterprise"
    ESSENTIALS = "Essentials"

    def visit(self, enterprise: typing.Callable[[], T_Result], essentials: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetBillingAccountResponsePlanType.ENTERPRISE:
            return enterprise()
        if self is GetBillingAccountResponsePlanType.ESSENTIALS:
            return essentials()
