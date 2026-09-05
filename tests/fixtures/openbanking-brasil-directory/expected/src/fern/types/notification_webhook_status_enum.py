

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationWebhookStatusEnum(enum.StrEnum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    DEACTIVATED = "Deactivated"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        confirmed: typing.Callable[[], T_Result],
        deactivated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NotificationWebhookStatusEnum.PENDING:
            return pending()
        if self is NotificationWebhookStatusEnum.CONFIRMED:
            return confirmed()
        if self is NotificationWebhookStatusEnum.DEACTIVATED:
            return deactivated()
