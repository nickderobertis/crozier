

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeTaintEffect(enum.StrEnum):
    """
    Kubernetes taint effect.
    """

    NO_SCHEDULE = "NoSchedule"
    PREFER_NO_SCHEDULE = "PreferNoSchedule"
    NO_EXECUTE = "NoExecute"

    def visit(
        self,
        no_schedule: typing.Callable[[], T_Result],
        prefer_no_schedule: typing.Callable[[], T_Result],
        no_execute: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NodeTaintEffect.NO_SCHEDULE:
            return no_schedule()
        if self is NodeTaintEffect.PREFER_NO_SCHEDULE:
            return prefer_no_schedule()
        if self is NodeTaintEffect.NO_EXECUTE:
            return no_execute()
