

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EntryMode(enum.StrEnum):
    """
    Entry mode of the payment details.
    """

    BOLETO = "BOLETO"
    SOFORT = "SOFORT"
    IDEAL = "IDEAL"
    BANCONTACT = "BANCONTACT"
    EPS = "EPS"
    MYBANK = "MYBANK"
    SATISPAY = "SATISPAY"
    BLIK = "BLIK"
    P24 = "P24"
    GIROPAY = "GIROPAY"
    PIX = "PIX"
    QR_CODE_PIX = "QR_CODE_PIX"
    APPLE_PAY = "APPLE_PAY"
    GOOGLE_PAY = "GOOGLE_PAY"
    PAYPAL = "PAYPAL"
    TWINT = "TWINT"
    NONE = "NONE"
    CHIP = "CHIP"
    MANUAL_ENTRY = "MANUAL_ENTRY"
    CUSTOMER_ENTRY = "CUSTOMER_ENTRY"
    MAGSTRIPE_FALLBACK = "MAGSTRIPE_FALLBACK"
    MAGSTRIPE = "MAGSTRIPE"
    DIRECT_DEBIT = "DIRECT_DEBIT"
    CONTACTLESS = "CONTACTLESS"
    MOTO = "MOTO"
    CONTACTLESS_MAGSTRIPE = "CONTACTLESS_MAGSTRIPE"
    NOT_APPLICABLE = "N/A"

    def visit(
        self,
        boleto: typing.Callable[[], T_Result],
        sofort: typing.Callable[[], T_Result],
        ideal: typing.Callable[[], T_Result],
        bancontact: typing.Callable[[], T_Result],
        eps: typing.Callable[[], T_Result],
        mybank: typing.Callable[[], T_Result],
        satispay: typing.Callable[[], T_Result],
        blik: typing.Callable[[], T_Result],
        p24: typing.Callable[[], T_Result],
        giropay: typing.Callable[[], T_Result],
        pix: typing.Callable[[], T_Result],
        qr_code_pix: typing.Callable[[], T_Result],
        apple_pay: typing.Callable[[], T_Result],
        google_pay: typing.Callable[[], T_Result],
        paypal: typing.Callable[[], T_Result],
        twint: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
        chip: typing.Callable[[], T_Result],
        manual_entry: typing.Callable[[], T_Result],
        customer_entry: typing.Callable[[], T_Result],
        magstripe_fallback: typing.Callable[[], T_Result],
        magstripe: typing.Callable[[], T_Result],
        direct_debit: typing.Callable[[], T_Result],
        contactless: typing.Callable[[], T_Result],
        moto: typing.Callable[[], T_Result],
        contactless_magstripe: typing.Callable[[], T_Result],
        not_applicable: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntryMode.BOLETO:
            return boleto()
        if self is EntryMode.SOFORT:
            return sofort()
        if self is EntryMode.IDEAL:
            return ideal()
        if self is EntryMode.BANCONTACT:
            return bancontact()
        if self is EntryMode.EPS:
            return eps()
        if self is EntryMode.MYBANK:
            return mybank()
        if self is EntryMode.SATISPAY:
            return satispay()
        if self is EntryMode.BLIK:
            return blik()
        if self is EntryMode.P24:
            return p24()
        if self is EntryMode.GIROPAY:
            return giropay()
        if self is EntryMode.PIX:
            return pix()
        if self is EntryMode.QR_CODE_PIX:
            return qr_code_pix()
        if self is EntryMode.APPLE_PAY:
            return apple_pay()
        if self is EntryMode.GOOGLE_PAY:
            return google_pay()
        if self is EntryMode.PAYPAL:
            return paypal()
        if self is EntryMode.TWINT:
            return twint()
        if self is EntryMode.NONE:
            return none()
        if self is EntryMode.CHIP:
            return chip()
        if self is EntryMode.MANUAL_ENTRY:
            return manual_entry()
        if self is EntryMode.CUSTOMER_ENTRY:
            return customer_entry()
        if self is EntryMode.MAGSTRIPE_FALLBACK:
            return magstripe_fallback()
        if self is EntryMode.MAGSTRIPE:
            return magstripe()
        if self is EntryMode.DIRECT_DEBIT:
            return direct_debit()
        if self is EntryMode.CONTACTLESS:
            return contactless()
        if self is EntryMode.MOTO:
            return moto()
        if self is EntryMode.CONTACTLESS_MAGSTRIPE:
            return contactless_magstripe()
        if self is EntryMode.NOT_APPLICABLE:
            return not_applicable()
