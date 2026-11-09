

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSessionsUsageRequestAggregate(enum.StrEnum):
    DEVICE = "device"
    FLEET = "fleet"
    PROJECT = "project"

    def visit(
        self,
        device: typing.Callable[[], T_Result],
        fleet: typing.Callable[[], T_Result],
        project: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSessionsUsageRequestAggregate.DEVICE:
            return device()
        if self is GetSessionsUsageRequestAggregate.FLEET:
            return fleet()
        if self is GetSessionsUsageRequestAggregate.PROJECT:
            return project()
