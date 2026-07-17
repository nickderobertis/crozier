

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemTierBandMethod(enum.StrEnum):
    """
    The methodology of how overdraft is charged. It can be:
    'Whole'  Where the same charge/rate is applied to the entirety of the overdraft balance (where charges are applicable).
    'Tiered' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount tiers defined by the lending financial organisation
    'Banded' Where different charges/rates are applied dependent on overdraft maximum and minimum balance amount bands defined by a government organisation.
    """

    INBA = "INBA"
    INTI = "INTI"
    INWH = "INWH"

    def visit(
        self,
        inba: typing.Callable[[], T_Result],
        inti: typing.Callable[[], T_Result],
        inwh: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemTierBandMethod.INBA:
            return inba()
        if self is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemTierBandMethod.INTI:
            return inti()
        if self is ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemTierBandMethod.INWH:
            return inwh()
