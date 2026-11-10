

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskCheckEmailDomainIsDisposable(enum.StrEnum):
    """
    Indicates whether the email domain is listed as disposable if known. Disposable domains are often used to create email addresses that are part of a fake set of user details.
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
        if self is RiskCheckEmailDomainIsDisposable.YES:
            return yes()
        if self is RiskCheckEmailDomainIsDisposable.NO:
            return no()
        if self is RiskCheckEmailDomainIsDisposable.NO_DATA:
            return no_data()
