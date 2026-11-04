

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProxyLocation(enum.StrEnum):
    RESIDENTIAL = "RESIDENTIAL"
    US_CA = "US-CA"
    US_NY = "US-NY"
    US_TX = "US-TX"
    US_FL = "US-FL"
    US_WA = "US-WA"
    RESIDENTIAL_ES = "RESIDENTIAL_ES"
    RESIDENTIAL_IE = "RESIDENTIAL_IE"
    RESIDENTIAL_GB = "RESIDENTIAL_GB"
    RESIDENTIAL_IN = "RESIDENTIAL_IN"
    RESIDENTIAL_JP = "RESIDENTIAL_JP"
    RESIDENTIAL_FR = "RESIDENTIAL_FR"
    RESIDENTIAL_DE = "RESIDENTIAL_DE"
    RESIDENTIAL_NZ = "RESIDENTIAL_NZ"
    RESIDENTIAL_ZA = "RESIDENTIAL_ZA"
    RESIDENTIAL_AR = "RESIDENTIAL_AR"
    RESIDENTIAL_AU = "RESIDENTIAL_AU"
    RESIDENTIAL_BR = "RESIDENTIAL_BR"
    RESIDENTIAL_TR = "RESIDENTIAL_TR"
    RESIDENTIAL_CA = "RESIDENTIAL_CA"
    RESIDENTIAL_MX = "RESIDENTIAL_MX"
    RESIDENTIAL_IT = "RESIDENTIAL_IT"
    RESIDENTIAL_NL = "RESIDENTIAL_NL"
    RESIDENTIAL_PH = "RESIDENTIAL_PH"
    RESIDENTIAL_KR = "RESIDENTIAL_KR"
    RESIDENTIAL_SA = "RESIDENTIAL_SA"
    RESIDENTIAL_ISP = "RESIDENTIAL_ISP"
    NONE = "NONE"

    def visit(
        self,
        residential: typing.Callable[[], T_Result],
        us_ca: typing.Callable[[], T_Result],
        us_ny: typing.Callable[[], T_Result],
        us_tx: typing.Callable[[], T_Result],
        us_fl: typing.Callable[[], T_Result],
        us_wa: typing.Callable[[], T_Result],
        residential_es: typing.Callable[[], T_Result],
        residential_ie: typing.Callable[[], T_Result],
        residential_gb: typing.Callable[[], T_Result],
        residential_in: typing.Callable[[], T_Result],
        residential_jp: typing.Callable[[], T_Result],
        residential_fr: typing.Callable[[], T_Result],
        residential_de: typing.Callable[[], T_Result],
        residential_nz: typing.Callable[[], T_Result],
        residential_za: typing.Callable[[], T_Result],
        residential_ar: typing.Callable[[], T_Result],
        residential_au: typing.Callable[[], T_Result],
        residential_br: typing.Callable[[], T_Result],
        residential_tr: typing.Callable[[], T_Result],
        residential_ca: typing.Callable[[], T_Result],
        residential_mx: typing.Callable[[], T_Result],
        residential_it: typing.Callable[[], T_Result],
        residential_nl: typing.Callable[[], T_Result],
        residential_ph: typing.Callable[[], T_Result],
        residential_kr: typing.Callable[[], T_Result],
        residential_sa: typing.Callable[[], T_Result],
        residential_isp: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProxyLocation.RESIDENTIAL:
            return residential()
        if self is ProxyLocation.US_CA:
            return us_ca()
        if self is ProxyLocation.US_NY:
            return us_ny()
        if self is ProxyLocation.US_TX:
            return us_tx()
        if self is ProxyLocation.US_FL:
            return us_fl()
        if self is ProxyLocation.US_WA:
            return us_wa()
        if self is ProxyLocation.RESIDENTIAL_ES:
            return residential_es()
        if self is ProxyLocation.RESIDENTIAL_IE:
            return residential_ie()
        if self is ProxyLocation.RESIDENTIAL_GB:
            return residential_gb()
        if self is ProxyLocation.RESIDENTIAL_IN:
            return residential_in()
        if self is ProxyLocation.RESIDENTIAL_JP:
            return residential_jp()
        if self is ProxyLocation.RESIDENTIAL_FR:
            return residential_fr()
        if self is ProxyLocation.RESIDENTIAL_DE:
            return residential_de()
        if self is ProxyLocation.RESIDENTIAL_NZ:
            return residential_nz()
        if self is ProxyLocation.RESIDENTIAL_ZA:
            return residential_za()
        if self is ProxyLocation.RESIDENTIAL_AR:
            return residential_ar()
        if self is ProxyLocation.RESIDENTIAL_AU:
            return residential_au()
        if self is ProxyLocation.RESIDENTIAL_BR:
            return residential_br()
        if self is ProxyLocation.RESIDENTIAL_TR:
            return residential_tr()
        if self is ProxyLocation.RESIDENTIAL_CA:
            return residential_ca()
        if self is ProxyLocation.RESIDENTIAL_MX:
            return residential_mx()
        if self is ProxyLocation.RESIDENTIAL_IT:
            return residential_it()
        if self is ProxyLocation.RESIDENTIAL_NL:
            return residential_nl()
        if self is ProxyLocation.RESIDENTIAL_PH:
            return residential_ph()
        if self is ProxyLocation.RESIDENTIAL_KR:
            return residential_kr()
        if self is ProxyLocation.RESIDENTIAL_SA:
            return residential_sa()
        if self is ProxyLocation.RESIDENTIAL_ISP:
            return residential_isp()
        if self is ProxyLocation.NONE:
            return none()
