

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObpcaData1OverdraftOverdraftTierBandSetItemTierBandMethod(str, enum.Enum):
    """
    The methodology of how overdraft is charged. It can be:
    'Whole'  Where the same charge/rate is applied to the entirety of the overdraft balance (where charges are applicable).
    'Tiered' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount tiers defined by the lending financial organisation
    'Banded' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount bands defined by a government organisation.
    """

    TIERED = "Tiered"
    WHOLE = "Whole"
    BANDED = "Banded"

    def visit(
        self,
        tiered: typing.Callable[[], T_Result],
        whole: typing.Callable[[], T_Result],
        banded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObpcaData1OverdraftOverdraftTierBandSetItemTierBandMethod.TIERED:
            return tiered()
        if self is ObpcaData1OverdraftOverdraftTierBandSetItemTierBandMethod.WHOLE:
            return whole()
        if self is ObpcaData1OverdraftOverdraftTierBandSetItemTierBandMethod.BANDED:
            return banded()
