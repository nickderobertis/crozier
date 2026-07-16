

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CheckoutOptionsPaymentType(enum.StrEnum):
    """ """

    CARD_PRESENT = "CARD_PRESENT"
    MANUAL_CARD_ENTRY = "MANUAL_CARD_ENTRY"
    FELICA_ID = "FELICA_ID"
    FELICA_QUICPAY = "FELICA_QUICPAY"
    FELICA_TRANSPORTATION_GROUP = "FELICA_TRANSPORTATION_GROUP"
    FELICA_ALL = "FELICA_ALL"

    def visit(
        self,
        card_present: typing.Callable[[], T_Result],
        manual_card_entry: typing.Callable[[], T_Result],
        felica_id: typing.Callable[[], T_Result],
        felica_quicpay: typing.Callable[[], T_Result],
        felica_transportation_group: typing.Callable[[], T_Result],
        felica_all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CheckoutOptionsPaymentType.CARD_PRESENT:
            return card_present()
        if self is CheckoutOptionsPaymentType.MANUAL_CARD_ENTRY:
            return manual_card_entry()
        if self is CheckoutOptionsPaymentType.FELICA_ID:
            return felica_id()
        if self is CheckoutOptionsPaymentType.FELICA_QUICPAY:
            return felica_quicpay()
        if self is CheckoutOptionsPaymentType.FELICA_TRANSPORTATION_GROUP:
            return felica_transportation_group()
        if self is CheckoutOptionsPaymentType.FELICA_ALL:
            return felica_all()
