

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManagedRiskRollingReserveAppliedNotificationRequestEnvironment(enum.StrEnum):
    """
    The environment from which the webhook originated.

    Possible values: **test**, **live**.
    """

    TEST = "test"
    LIVE = "live"

    def visit(self, test: typing.Callable[[], T_Result], live: typing.Callable[[], T_Result]) -> T_Result:
        if self is ManagedRiskRollingReserveAppliedNotificationRequestEnvironment.TEST:
            return test()
        if self is ManagedRiskRollingReserveAppliedNotificationRequestEnvironment.LIVE:
            return live()
