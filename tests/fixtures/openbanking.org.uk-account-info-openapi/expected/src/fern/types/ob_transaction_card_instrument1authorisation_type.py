

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObTransactionCardInstrument1AuthorisationType(str, enum.Enum):
    """
    The card authorisation type.
    """

    CONSUMER_DEVICE = "ConsumerDevice"
    CONTACTLESS = "Contactless"
    NONE = "None"
    PIN = "PIN"

    def visit(
        self,
        consumer_device: typing.Callable[[], T_Result],
        contactless: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
        pin: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObTransactionCardInstrument1AuthorisationType.CONSUMER_DEVICE:
            return consumer_device()
        if self is ObTransactionCardInstrument1AuthorisationType.CONTACTLESS:
            return contactless()
        if self is ObTransactionCardInstrument1AuthorisationType.NONE:
            return none()
        if self is ObTransactionCardInstrument1AuthorisationType.PIN:
            return pin()
