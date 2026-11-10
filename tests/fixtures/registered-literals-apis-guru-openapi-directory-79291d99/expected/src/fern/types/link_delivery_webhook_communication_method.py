

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkDeliveryWebhookCommunicationMethod(enum.StrEnum):
    """
    The communication method used to deliver the hosted link session
    """

    SMS = "sms"
    EMAIL = "email"

    def visit(self, sms: typing.Callable[[], T_Result], email: typing.Callable[[], T_Result]) -> T_Result:
        if self is LinkDeliveryWebhookCommunicationMethod.SMS:
            return sms()
        if self is LinkDeliveryWebhookCommunicationMethod.EMAIL:
            return email()
