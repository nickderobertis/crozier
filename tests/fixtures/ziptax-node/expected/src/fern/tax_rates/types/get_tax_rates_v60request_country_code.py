

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetTaxRatesV60RequestCountryCode(enum.StrEnum):
    """
    Country of the lookup: 'USA' (default), 'CAN', or a US territory (ASM, GUM, MNP, PRI, VIR). 'CAN' requires the Canadian rates (rate_loc_can) entitlement; otherwise the request returns response code 112. US territories are looked up via the USA path and require no additional entitlement.
    """

    USA = "USA"
    CAN = "CAN"
    PRI = "PRI"
    ASM = "ASM"
    GUM = "GUM"
    MNP = "MNP"
    VIR = "VIR"

    def visit(
        self,
        usa: typing.Callable[[], T_Result],
        can: typing.Callable[[], T_Result],
        pri: typing.Callable[[], T_Result],
        asm: typing.Callable[[], T_Result],
        gum: typing.Callable[[], T_Result],
        mnp: typing.Callable[[], T_Result],
        vir: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetTaxRatesV60RequestCountryCode.USA:
            return usa()
        if self is GetTaxRatesV60RequestCountryCode.CAN:
            return can()
        if self is GetTaxRatesV60RequestCountryCode.PRI:
            return pri()
        if self is GetTaxRatesV60RequestCountryCode.ASM:
            return asm()
        if self is GetTaxRatesV60RequestCountryCode.GUM:
            return gum()
        if self is GetTaxRatesV60RequestCountryCode.MNP:
            return mnp()
        if self is GetTaxRatesV60RequestCountryCode.VIR:
            return vir()
