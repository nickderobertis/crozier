

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CircuitStatusLabel(enum.StrEnum):
    PLANNED = "Planned"
    PROVISIONING = "Provisioning"
    ACTIVE = "Active"
    OFFLINE = "Offline"
    DEPROVISIONING = "Deprovisioning"
    DECOMMISSIONED = "Decommissioned"

    def visit(
        self,
        planned: typing.Callable[[], T_Result],
        provisioning: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        offline: typing.Callable[[], T_Result],
        deprovisioning: typing.Callable[[], T_Result],
        decommissioned: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CircuitStatusLabel.PLANNED:
            return planned()
        if self is CircuitStatusLabel.PROVISIONING:
            return provisioning()
        if self is CircuitStatusLabel.ACTIVE:
            return active()
        if self is CircuitStatusLabel.OFFLINE:
            return offline()
        if self is CircuitStatusLabel.DEPROVISIONING:
            return deprovisioning()
        if self is CircuitStatusLabel.DECOMMISSIONED:
            return decommissioned()
