

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InvoiceDeliveryMethod(str, enum.Enum):
    """
    Indicates how Square delivers the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to the customer.
    """

    EMAIL = "EMAIL"
    SHARE_MANUALLY = "SHARE_MANUALLY"
    SMS = "SMS"

    def visit(
        self,
        email: typing.Callable[[], T_Result],
        share_manually: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceDeliveryMethod.EMAIL:
            return email()
        if self is InvoiceDeliveryMethod.SHARE_MANUALLY:
            return share_manually()
        if self is InvoiceDeliveryMethod.SMS:
            return sms()
