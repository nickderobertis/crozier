

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InvoiceRequestMethod(str, enum.Enum):
    """
    Specifies the action for Square to take for processing the invoice. For example,
    email the invoice, charge a customer's card on file, or do nothing. DEPRECATED at
    version 2021-01-21. The corresponding `request_method` field is replaced by the
    `Invoice.delivery_method` and `InvoicePaymentRequest.automatic_payment_source` fields.
    """

    EMAIL = "EMAIL"
    CHARGE_CARD_ON_FILE = "CHARGE_CARD_ON_FILE"
    SHARE_MANUALLY = "SHARE_MANUALLY"
    CHARGE_BANK_ON_FILE = "CHARGE_BANK_ON_FILE"
    SMS = "SMS"
    SMS_CHARGE_CARD_ON_FILE = "SMS_CHARGE_CARD_ON_FILE"
    SMS_CHARGE_BANK_ON_FILE = "SMS_CHARGE_BANK_ON_FILE"

    def visit(
        self,
        email: typing.Callable[[], T_Result],
        charge_card_on_file: typing.Callable[[], T_Result],
        share_manually: typing.Callable[[], T_Result],
        charge_bank_on_file: typing.Callable[[], T_Result],
        sms: typing.Callable[[], T_Result],
        sms_charge_card_on_file: typing.Callable[[], T_Result],
        sms_charge_bank_on_file: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceRequestMethod.EMAIL:
            return email()
        if self is InvoiceRequestMethod.CHARGE_CARD_ON_FILE:
            return charge_card_on_file()
        if self is InvoiceRequestMethod.SHARE_MANUALLY:
            return share_manually()
        if self is InvoiceRequestMethod.CHARGE_BANK_ON_FILE:
            return charge_bank_on_file()
        if self is InvoiceRequestMethod.SMS:
            return sms()
        if self is InvoiceRequestMethod.SMS_CHARGE_CARD_ON_FILE:
            return sms_charge_card_on_file()
        if self is InvoiceRequestMethod.SMS_CHARGE_BANK_ON_FILE:
            return sms_charge_bank_on_file()
