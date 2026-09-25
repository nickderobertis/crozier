

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListWebhookEventsResponseEventsItemDeliveryStatus(enum.StrEnum):
    """
    Delivery status of the webhook
    """

    QUEUED = "QUEUED"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    DROPPED = "DROPPED"

    def visit(
        self,
        queued: typing.Callable[[], T_Result],
        succeeded: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        dropped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListWebhookEventsResponseEventsItemDeliveryStatus.QUEUED:
            return queued()
        if self is ListWebhookEventsResponseEventsItemDeliveryStatus.SUCCEEDED:
            return succeeded()
        if self is ListWebhookEventsResponseEventsItemDeliveryStatus.FAILED:
            return failed()
        if self is ListWebhookEventsResponseEventsItemDeliveryStatus.DROPPED:
            return dropped()
