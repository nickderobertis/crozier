

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LinkDeliveryDeliveryMethod(enum.StrEnum):
    """
    The delivery method to be used to deliver the Link Delivery URL.

    `SMS`: The URL will be delivered through SMS

    `EMAIL`: The URL will be delivered through email
    """

    SMS = "SMS"
    EMAIL = "EMAIL"

    def visit(self, sms: typing.Callable[[], T_Result], email: typing.Callable[[], T_Result]) -> T_Result:
        if self is LinkDeliveryDeliveryMethod.SMS:
            return sms()
        if self is LinkDeliveryDeliveryMethod.EMAIL:
            return email()
