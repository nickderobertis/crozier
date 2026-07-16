

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObTransactionCardInstrument1CardSchemeName(str, enum.Enum):
    """
    Name of the card scheme.
    """

    AMERICAN_EXPRESS = "AmericanExpress"
    DINERS = "Diners"
    DISCOVER = "Discover"
    MASTER_CARD = "MasterCard"
    VISA = "VISA"

    def visit(
        self,
        american_express: typing.Callable[[], T_Result],
        diners: typing.Callable[[], T_Result],
        discover: typing.Callable[[], T_Result],
        master_card: typing.Callable[[], T_Result],
        visa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObTransactionCardInstrument1CardSchemeName.AMERICAN_EXPRESS:
            return american_express()
        if self is ObTransactionCardInstrument1CardSchemeName.DINERS:
            return diners()
        if self is ObTransactionCardInstrument1CardSchemeName.DISCOVER:
            return discover()
        if self is ObTransactionCardInstrument1CardSchemeName.MASTER_CARD:
            return master_card()
        if self is ObTransactionCardInstrument1CardSchemeName.VISA:
            return visa()
