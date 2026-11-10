

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskCheckEmailTopLevelDomainIsSuspicious(enum.StrEnum):
    """
    Indicates whether the email address top level domain, which is the last part of the domain, is fraudulent or risky if known. In most cases, a suspicious top level domain is also associated with a disposable or high-risk domain.
    """

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    def visit(
        self,
        yes: typing.Callable[[], T_Result],
        no: typing.Callable[[], T_Result],
        no_data: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskCheckEmailTopLevelDomainIsSuspicious.YES:
            return yes()
        if self is RiskCheckEmailTopLevelDomainIsSuspicious.NO:
            return no()
        if self is RiskCheckEmailTopLevelDomainIsSuspicious.NO_DATA:
            return no_data()
