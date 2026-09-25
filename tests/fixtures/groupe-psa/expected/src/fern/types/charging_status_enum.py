

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChargingStatusEnum(enum.StrEnum):
    """
    status of charging system.
    """

    DISCONNECTED = "Disconnected"
    IN_PROGRESS = "InProgress"
    FAILURE = "Failure"
    STOPPED = "Stopped"
    FINISHED = "Finished"

    def visit(
        self,
        disconnected: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        failure: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        finished: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChargingStatusEnum.DISCONNECTED:
            return disconnected()
        if self is ChargingStatusEnum.IN_PROGRESS:
            return in_progress()
        if self is ChargingStatusEnum.FAILURE:
            return failure()
        if self is ChargingStatusEnum.STOPPED:
            return stopped()
        if self is ChargingStatusEnum.FINISHED:
            return finished()
