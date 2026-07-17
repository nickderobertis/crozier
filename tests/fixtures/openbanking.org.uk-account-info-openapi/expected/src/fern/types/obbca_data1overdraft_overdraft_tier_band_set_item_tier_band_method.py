

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1OverdraftOverdraftTierBandSetItemTierBandMethod(enum.StrEnum):
    """
    The methodology of how overdraft is charged. It can be:
    'Whole'  Where the same charge/rate is applied to the entirety of the overdraft balance (where charges are applicable).
    'Tiered' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount tiers defined by the lending financial organisation
    'Banded' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount bands defined by a government organisation.
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
        if self is ObbcaData1OverdraftOverdraftTierBandSetItemTierBandMethod.BANDED:
            return banded()
        if self is ObbcaData1OverdraftOverdraftTierBandSetItemTierBandMethod.TIERED:
            return tiered()
        if self is ObbcaData1OverdraftOverdraftTierBandSetItemTierBandMethod.WHOLE:
            return whole()
