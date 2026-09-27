

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompanySize(enum.StrEnum):
    """
    A range representing the number of people working at the company
    """

    ONE10 = "1-10"
    ELEVEN50 = "11-50"
    FIFTY_ONE200 = "51-200"
    TWO_HUNDRED_ONE500 = "201-500"
    FIVE_HUNDRED_ONE1000 = "501-1000"
    ONE_THOUSAND_ONE5000 = "1001-5000"
    FIVE_THOUSAND_ONE10000 = "5001-10000"
    UNDEFINED = "10001+"

    def visit(
        self,
        one10: typing.Callable[[], T_Result],
        eleven50: typing.Callable[[], T_Result],
        fifty_one200: typing.Callable[[], T_Result],
        two_hundred_one500: typing.Callable[[], T_Result],
        five_hundred_one1000: typing.Callable[[], T_Result],
        one_thousand_one5000: typing.Callable[[], T_Result],
        five_thousand_one10000: typing.Callable[[], T_Result],
        undefined: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CompanySize.ONE10:
            return one10()
        if self is CompanySize.ELEVEN50:
            return eleven50()
        if self is CompanySize.FIFTY_ONE200:
            return fifty_one200()
        if self is CompanySize.TWO_HUNDRED_ONE500:
            return two_hundred_one500()
        if self is CompanySize.FIVE_HUNDRED_ONE1000:
            return five_hundred_one1000()
        if self is CompanySize.ONE_THOUSAND_ONE5000:
            return one_thousand_one5000()
        if self is CompanySize.FIVE_THOUSAND_ONE10000:
            return five_thousand_one10000()
        if self is CompanySize.UNDEFINED:
            return undefined()
