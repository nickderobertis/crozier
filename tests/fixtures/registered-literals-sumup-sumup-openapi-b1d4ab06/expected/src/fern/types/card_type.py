

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CardType(enum.StrEnum):
    """
    Issuing card network of the payment card used for the transaction.
    """

    ALELO = "ALELO"
    AMEX = "AMEX"
    CONECS = "CONECS"
    CUP = "CUP"
    DINERS = "DINERS"
    DISCOVER = "DISCOVER"
    EFTPOS = "EFTPOS"
    ELO = "ELO"
    ELV = "ELV"
    GIROCARD = "GIROCARD"
    HIPERCARD = "HIPERCARD"
    INTERAC = "INTERAC"
    JCB = "JCB"
    MAESTRO = "MAESTRO"
    MASTERCARD = "MASTERCARD"
    PLUXEE = "PLUXEE"
    SWILE = "SWILE"
    TICKET = "TICKET"
    VISA = "VISA"
    VISA_ELECTRON = "VISA_ELECTRON"
    VISA_VPAY = "VISA_VPAY"
    VPAY = "VPAY"
    VR = "VR"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        alelo: typing.Callable[[], T_Result],
        amex: typing.Callable[[], T_Result],
        conecs: typing.Callable[[], T_Result],
        cup: typing.Callable[[], T_Result],
        diners: typing.Callable[[], T_Result],
        discover: typing.Callable[[], T_Result],
        eftpos: typing.Callable[[], T_Result],
        elo: typing.Callable[[], T_Result],
        elv: typing.Callable[[], T_Result],
        girocard: typing.Callable[[], T_Result],
        hipercard: typing.Callable[[], T_Result],
        interac: typing.Callable[[], T_Result],
        jcb: typing.Callable[[], T_Result],
        maestro: typing.Callable[[], T_Result],
        mastercard: typing.Callable[[], T_Result],
        pluxee: typing.Callable[[], T_Result],
        swile: typing.Callable[[], T_Result],
        ticket: typing.Callable[[], T_Result],
        visa: typing.Callable[[], T_Result],
        visa_electron: typing.Callable[[], T_Result],
        visa_vpay: typing.Callable[[], T_Result],
        vpay: typing.Callable[[], T_Result],
        vr: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CardType.ALELO:
            return alelo()
        if self is CardType.AMEX:
            return amex()
        if self is CardType.CONECS:
            return conecs()
        if self is CardType.CUP:
            return cup()
        if self is CardType.DINERS:
            return diners()
        if self is CardType.DISCOVER:
            return discover()
        if self is CardType.EFTPOS:
            return eftpos()
        if self is CardType.ELO:
            return elo()
        if self is CardType.ELV:
            return elv()
        if self is CardType.GIROCARD:
            return girocard()
        if self is CardType.HIPERCARD:
            return hipercard()
        if self is CardType.INTERAC:
            return interac()
        if self is CardType.JCB:
            return jcb()
        if self is CardType.MAESTRO:
            return maestro()
        if self is CardType.MASTERCARD:
            return mastercard()
        if self is CardType.PLUXEE:
            return pluxee()
        if self is CardType.SWILE:
            return swile()
        if self is CardType.TICKET:
            return ticket()
        if self is CardType.VISA:
            return visa()
        if self is CardType.VISA_ELECTRON:
            return visa_electron()
        if self is CardType.VISA_VPAY:
            return visa_vpay()
        if self is CardType.VPAY:
            return vpay()
        if self is CardType.VR:
            return vr()
        if self is CardType.UNKNOWN:
            return unknown()
