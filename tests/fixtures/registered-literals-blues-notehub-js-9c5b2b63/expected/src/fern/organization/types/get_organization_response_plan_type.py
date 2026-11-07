

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetOrganizationResponsePlanType(enum.StrEnum):
    ENTERPRISE = "Enterprise"
    ESSENTIALS = "Essentials"

    def visit(self, enterprise: typing.Callable[[], T_Result], essentials: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetOrganizationResponsePlanType.ENTERPRISE:
            return enterprise()
        if self is GetOrganizationResponsePlanType.ESSENTIALS:
            return essentials()
