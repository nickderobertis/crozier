

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1Alpha1TriggerRuleType(enum.StrEnum):
    SCHEDULE = "schedule"
    CONDITION = "condition"

    def visit(self, schedule: typing.Callable[[], T_Result], condition: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1Alpha1TriggerRuleType.SCHEDULE:
            return schedule()
        if self is V1Alpha1TriggerRuleType.CONDITION:
            return condition()
