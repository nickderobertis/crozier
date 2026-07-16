

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftType(enum.StrEnum):
    """
    An overdraft can either be 'committed' which means that the facility cannot be withdrawn without reasonable notification before it's agreed end date, or 'on demand' which means that the financial institution can demand repayment at any point in time.
    """

    COMMITTED = "Committed"
    ON_DEMAND = "OnDemand"

    def visit(self, committed: typing.Callable[[], T_Result], on_demand: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftType.COMMITTED:
            return committed()
        if self is ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftType.ON_DEMAND:
            return on_demand()
