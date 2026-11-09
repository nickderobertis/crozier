

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDataUsageRequestAggregate(enum.StrEnum):
    DEVICE = "device"
    FLEET = "fleet"
    PROJECT = "project"

    def visit(
        self,
        device: typing.Callable[[], T_Result],
        fleet: typing.Callable[[], T_Result],
        project: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDataUsageRequestAggregate.DEVICE:
            return device()
        if self is GetDataUsageRequestAggregate.FLEET:
            return fleet()
        if self is GetDataUsageRequestAggregate.PROJECT:
            return project()
