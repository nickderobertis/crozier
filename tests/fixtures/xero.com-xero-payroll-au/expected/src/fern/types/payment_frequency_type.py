

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PaymentFrequencyType(str, enum.Enum):
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    FORTNIGHTLY = "FORTNIGHTLY"
    QUARTERLY = "QUARTERLY"
    TWICEMONTHLY = "TWICEMONTHLY"
    FOURWEEKLY = "FOURWEEKLY"
    YEARLY = "YEARLY"

    def visit(
        self,
        weekly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
        fortnightly: typing.Callable[[], T_Result],
        quarterly: typing.Callable[[], T_Result],
        twicemonthly: typing.Callable[[], T_Result],
        fourweekly: typing.Callable[[], T_Result],
        yearly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PaymentFrequencyType.WEEKLY:
            return weekly()
        if self is PaymentFrequencyType.MONTHLY:
            return monthly()
        if self is PaymentFrequencyType.FORTNIGHTLY:
            return fortnightly()
        if self is PaymentFrequencyType.QUARTERLY:
            return quarterly()
        if self is PaymentFrequencyType.TWICEMONTHLY:
            return twicemonthly()
        if self is PaymentFrequencyType.FOURWEEKLY:
            return fourweekly()
        if self is PaymentFrequencyType.YEARLY:
            return yearly()
