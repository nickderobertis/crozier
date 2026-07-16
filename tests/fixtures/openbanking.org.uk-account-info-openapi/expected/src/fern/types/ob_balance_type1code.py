

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObBalanceType1Code(str, enum.Enum):
    """
    Balance type, in a coded form.
    """

    CLOSING_AVAILABLE = "ClosingAvailable"
    CLOSING_BOOKED = "ClosingBooked"
    CLOSING_CLEARED = "ClosingCleared"
    EXPECTED = "Expected"
    FORWARD_AVAILABLE = "ForwardAvailable"
    INFORMATION = "Information"
    INTERIM_AVAILABLE = "InterimAvailable"
    INTERIM_BOOKED = "InterimBooked"
    INTERIM_CLEARED = "InterimCleared"
    OPENING_AVAILABLE = "OpeningAvailable"
    OPENING_BOOKED = "OpeningBooked"
    OPENING_CLEARED = "OpeningCleared"
    PREVIOUSLY_CLOSED_BOOKED = "PreviouslyClosedBooked"

    def visit(
        self,
        closing_available: typing.Callable[[], T_Result],
        closing_booked: typing.Callable[[], T_Result],
        closing_cleared: typing.Callable[[], T_Result],
        expected: typing.Callable[[], T_Result],
        forward_available: typing.Callable[[], T_Result],
        information: typing.Callable[[], T_Result],
        interim_available: typing.Callable[[], T_Result],
        interim_booked: typing.Callable[[], T_Result],
        interim_cleared: typing.Callable[[], T_Result],
        opening_available: typing.Callable[[], T_Result],
        opening_booked: typing.Callable[[], T_Result],
        opening_cleared: typing.Callable[[], T_Result],
        previously_closed_booked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObBalanceType1Code.CLOSING_AVAILABLE:
            return closing_available()
        if self is ObBalanceType1Code.CLOSING_BOOKED:
            return closing_booked()
        if self is ObBalanceType1Code.CLOSING_CLEARED:
            return closing_cleared()
        if self is ObBalanceType1Code.EXPECTED:
            return expected()
        if self is ObBalanceType1Code.FORWARD_AVAILABLE:
            return forward_available()
        if self is ObBalanceType1Code.INFORMATION:
            return information()
        if self is ObBalanceType1Code.INTERIM_AVAILABLE:
            return interim_available()
        if self is ObBalanceType1Code.INTERIM_BOOKED:
            return interim_booked()
        if self is ObBalanceType1Code.INTERIM_CLEARED:
            return interim_cleared()
        if self is ObBalanceType1Code.OPENING_AVAILABLE:
            return opening_available()
        if self is ObBalanceType1Code.OPENING_BOOKED:
            return opening_booked()
        if self is ObBalanceType1Code.OPENING_CLEARED:
            return opening_cleared()
        if self is ObBalanceType1Code.PREVIOUSLY_CLOSED_BOOKED:
            return previously_closed_booked()
