

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InvoiceAutomaticPaymentSource(str, enum.Enum):
    """
    Indicates the automatic payment method for an [invoice payment request](https://developer.squareup.com/reference/square_2021-08-18/objects/InvoicePaymentRequest).
    """

    NONE = "NONE"
    CARD_ON_FILE = "CARD_ON_FILE"
    BANK_ON_FILE = "BANK_ON_FILE"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        card_on_file: typing.Callable[[], T_Result],
        bank_on_file: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceAutomaticPaymentSource.NONE:
            return none()
        if self is InvoiceAutomaticPaymentSource.CARD_ON_FILE:
            return card_on_file()
        if self is InvoiceAutomaticPaymentSource.BANK_ON_FILE:
            return bank_on_file()
