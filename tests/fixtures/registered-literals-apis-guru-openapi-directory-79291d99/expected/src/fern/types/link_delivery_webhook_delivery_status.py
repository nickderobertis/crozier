

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkDeliveryWebhookDeliveryStatus(enum.StrEnum):
    """
    The status of the delivery of the hosted link to the user
    """

    SUCCEEDED = "succeeded"
    FAILED = "failed"

    def visit(self, succeeded: typing.Callable[[], T_Result], failed: typing.Callable[[], T_Result]) -> T_Result:
        if self is LinkDeliveryWebhookDeliveryStatus.SUCCEEDED:
            return succeeded()
        if self is LinkDeliveryWebhookDeliveryStatus.FAILED:
            return failed()
