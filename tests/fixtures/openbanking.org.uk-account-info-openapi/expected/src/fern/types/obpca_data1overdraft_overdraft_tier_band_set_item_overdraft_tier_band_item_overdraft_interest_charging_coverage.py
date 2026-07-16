

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage(enum.StrEnum):
    """
    Interest charged on whole amount or tiered/banded
    """

    TIERED = "Tiered"
    WHOLE = "Whole"

    def visit(self, tiered: typing.Callable[[], T_Result], whole: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage.TIERED
        ):
            return tiered()
        if (
            self
            is ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage.WHOLE
        ):
            return whole()
