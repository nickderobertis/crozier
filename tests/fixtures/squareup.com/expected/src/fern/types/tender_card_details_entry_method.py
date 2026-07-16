

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TenderCardDetailsEntryMethod(str, enum.Enum):
    """
    Indicates the method used to enter the card's details.
    """

    SWIPED = "SWIPED"
    KEYED = "KEYED"
    EMV = "EMV"
    ON_FILE = "ON_FILE"
    CONTACTLESS = "CONTACTLESS"

    def visit(
        self,
        swiped: typing.Callable[[], T_Result],
        keyed: typing.Callable[[], T_Result],
        emv: typing.Callable[[], T_Result],
        on_file: typing.Callable[[], T_Result],
        contactless: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TenderCardDetailsEntryMethod.SWIPED:
            return swiped()
        if self is TenderCardDetailsEntryMethod.KEYED:
            return keyed()
        if self is TenderCardDetailsEntryMethod.EMV:
            return emv()
        if self is TenderCardDetailsEntryMethod.ON_FILE:
            return on_file()
        if self is TenderCardDetailsEntryMethod.CONTACTLESS:
            return contactless()
