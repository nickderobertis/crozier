

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskCheckEmailDomainIsFreeProvider(enum.StrEnum):
    """
    Indicates whether the email address domain is a free provider such as Gmail or Hotmail if known.
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
        if self is RiskCheckEmailDomainIsFreeProvider.YES:
            return yes()
        if self is RiskCheckEmailDomainIsFreeProvider.NO:
            return no()
        if self is RiskCheckEmailDomainIsFreeProvider.NO_DATA:
            return no_data()
