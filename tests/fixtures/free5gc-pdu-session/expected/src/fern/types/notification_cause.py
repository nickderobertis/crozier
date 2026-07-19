

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationCause(enum.StrEnum):
    QOS_FULFILLED = "QOS_FULFILLED"
    QOS_NOT_FULFILLED = "QOS_NOT_FULFILLED"
    UP_SEC_FULFILLED = "UP_SEC_FULFILLED"
    UP_SEC_NOT_FULFILLED = "UP_SEC_NOT_FULFILLED"

    def visit(
        self,
        qos_fulfilled: typing.Callable[[], T_Result],
        qos_not_fulfilled: typing.Callable[[], T_Result],
        up_sec_fulfilled: typing.Callable[[], T_Result],
        up_sec_not_fulfilled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NotificationCause.QOS_FULFILLED:
            return qos_fulfilled()
        if self is NotificationCause.QOS_NOT_FULFILLED:
            return qos_not_fulfilled()
        if self is NotificationCause.UP_SEC_FULFILLED:
            return up_sec_fulfilled()
        if self is NotificationCause.UP_SEC_NOT_FULFILLED:
            return up_sec_not_fulfilled()
