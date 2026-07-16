

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritableCircuitStatus(str, enum.Enum):
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
        if self is WritableCircuitStatus.PLANNED:
            return planned()
        if self is WritableCircuitStatus.PROVISIONING:
            return provisioning()
        if self is WritableCircuitStatus.ACTIVE:
            return active()
        if self is WritableCircuitStatus.OFFLINE:
            return offline()
        if self is WritableCircuitStatus.DEPROVISIONING:
            return deprovisioning()
        if self is WritableCircuitStatus.DECOMMISSIONED:
            return decommissioned()
