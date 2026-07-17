

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CircuitStatusValue(enum.StrEnum):
    PLANNED = "planned"
    PROVISIONING = "provisioning"
    ACTIVE = "active"
    OFFLINE = "offline"
    DEPROVISIONING = "deprovisioning"
    DECOMMISSIONED = "decommissioned"

    def visit(
        self,
        planned: typing.Callable[[], T_Result],
        provisioning: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        offline: typing.Callable[[], T_Result],
        deprovisioning: typing.Callable[[], T_Result],
        decommissioned: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CircuitStatusValue.PLANNED:
            return planned()
        if self is CircuitStatusValue.PROVISIONING:
            return provisioning()
        if self is CircuitStatusValue.ACTIVE:
            return active()
        if self is CircuitStatusValue.OFFLINE:
            return offline()
        if self is CircuitStatusValue.DEPROVISIONING:
            return deprovisioning()
        if self is CircuitStatusValue.DECOMMISSIONED:
            return decommissioned()
