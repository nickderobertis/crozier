

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1CreditInterestTierBandSetItemTierBandMethod(enum.StrEnum):
    """
    The methodology of how credit interest is paid/applied. It can be:-

    1. Banded
    Interest rates are banded. i.e. Increasing rate on whole balance as balance increases.

    2. Tiered
    Interest rates are tiered. i.e. increasing rate for each tier as balance increases, but interest paid on tier fixed for that tier and not on whole balance.

    3. Whole
    The same interest rate is applied irrespective of the BCA balance
    """

    BANDED = "Banded"
    TIERED = "Tiered"
    WHOLE = "Whole"

    def visit(
        self,
        banded: typing.Callable[[], T_Result],
        tiered: typing.Callable[[], T_Result],
        whole: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandMethod.BANDED:
            return banded()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandMethod.TIERED:
            return tiered()
        if self is ObbcaData1CreditInterestTierBandSetItemTierBandMethod.WHOLE:
            return whole()
