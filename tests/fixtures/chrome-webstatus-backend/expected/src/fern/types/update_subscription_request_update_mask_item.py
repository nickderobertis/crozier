

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateSubscriptionRequestUpdateMaskItem(enum.StrEnum):
    TRIGGERS = "triggers"
    FREQUENCY = "frequency"

    def visit(self, triggers: typing.Callable[[], T_Result], frequency: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateSubscriptionRequestUpdateMaskItem.TRIGGERS:
            return triggers()
        if self is UpdateSubscriptionRequestUpdateMaskItem.FREQUENCY:
            return frequency()
