

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftType(enum.StrEnum):
    """
    An overdraft can either be 'committed' which means that the facility cannot be withdrawn without reasonable notification before it's agreed end date, or 'on demand' which means that the financial institution can demand repayment at any point in time.
    """

    COMMITTED = "Committed"
    ON_DEMAND = "OnDemand"
    OTHER = "Other"

    def visit(
        self,
        committed: typing.Callable[[], T_Result],
        on_demand: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftType.COMMITTED:
            return committed()
        if self is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftType.ON_DEMAND:
            return on_demand()
        if self is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftType.OTHER:
            return other()
