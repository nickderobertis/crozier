

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskCheckEmailIsDeliverableStatus(enum.StrEnum):
    """
    SMTP-MX check to confirm the email address exists if known.
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
        if self is RiskCheckEmailIsDeliverableStatus.YES:
            return yes()
        if self is RiskCheckEmailIsDeliverableStatus.NO:
            return no()
        if self is RiskCheckEmailIsDeliverableStatus.NO_DATA:
            return no_data()
