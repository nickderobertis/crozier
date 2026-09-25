

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertRuleNotificationConfigModelFrequency(enum.StrEnum):
    AS_IT_HAPPENS = "as_it_happens"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

    def visit(
        self,
        as_it_happens: typing.Callable[[], T_Result],
        daily: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlertRuleNotificationConfigModelFrequency.AS_IT_HAPPENS:
            return as_it_happens()
        if self is AlertRuleNotificationConfigModelFrequency.DAILY:
            return daily()
        if self is AlertRuleNotificationConfigModelFrequency.WEEKLY:
            return weekly()
        if self is AlertRuleNotificationConfigModelFrequency.MONTHLY:
            return monthly()
