

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PreconditioningBaseAirConditioningStatus(enum.StrEnum):
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
        if self is PreconditioningBaseAirConditioningStatus.ENABLED:
            return enabled()
        if self is PreconditioningBaseAirConditioningStatus.DISABLED:
            return disabled()
        if self is PreconditioningBaseAirConditioningStatus.FINISHED:
            return finished()
        if self is PreconditioningBaseAirConditioningStatus.FAILURE:
            return failure()
