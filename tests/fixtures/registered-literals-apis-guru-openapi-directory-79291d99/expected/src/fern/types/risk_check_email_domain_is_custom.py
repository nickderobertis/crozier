

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskCheckEmailDomainIsCustom(enum.StrEnum):
    """
    Indicates whether the email address domain is custom if known, i.e. a company domain and not free or disposable.
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
        if self is RiskCheckEmailDomainIsCustom.YES:
            return yes()
        if self is RiskCheckEmailDomainIsCustom.NO:
            return no()
        if self is RiskCheckEmailDomainIsCustom.NO_DATA:
            return no_data()
