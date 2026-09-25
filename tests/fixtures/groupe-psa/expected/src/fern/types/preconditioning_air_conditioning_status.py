

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreconditioningAirConditioningStatus(enum.StrEnum):
    """
    The status of the preconditioning feature.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    FINISHED = "Finished"
    FAILURE = "Failure"

    def visit(
        self,
        enabled: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        finished: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PreconditioningAirConditioningStatus.ENABLED:
            return enabled()
        if self is PreconditioningAirConditioningStatus.DISABLED:
            return disabled()
        if self is PreconditioningAirConditioningStatus.FINISHED:
            return finished()
        if self is PreconditioningAirConditioningStatus.FAILURE:
            return failure()
