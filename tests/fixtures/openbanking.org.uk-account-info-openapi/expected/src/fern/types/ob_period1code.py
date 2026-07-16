

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObPeriod1Code(str, enum.Enum):
    """
    Period e.g. day, week, month etc. for which the fee/charge is capped
    """

    PACT = "PACT"
    PDAY = "PDAY"
    PHYR = "PHYR"
    PMTH = "PMTH"
    PQTR = "PQTR"
    PWEK = "PWEK"
    PYER = "PYER"

    def visit(
        self,
        pact: typing.Callable[[], T_Result],
        pday: typing.Callable[[], T_Result],
        phyr: typing.Callable[[], T_Result],
        pmth: typing.Callable[[], T_Result],
        pqtr: typing.Callable[[], T_Result],
        pwek: typing.Callable[[], T_Result],
        pyer: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObPeriod1Code.PACT:
            return pact()
        if self is ObPeriod1Code.PDAY:
            return pday()
        if self is ObPeriod1Code.PHYR:
            return phyr()
        if self is ObPeriod1Code.PMTH:
            return pmth()
        if self is ObPeriod1Code.PQTR:
            return pqtr()
        if self is ObPeriod1Code.PWEK:
            return pwek()
        if self is ObPeriod1Code.PYER:
            return pyer()
